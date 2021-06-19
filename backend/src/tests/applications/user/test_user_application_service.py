from uuid import uuid4, UUID

from container import injector

from tests.test_case_impl import TestCaseImpl

from applications.error import Error
from applications.user.user_application_service import UserApplicationService
from applications.user.get_user_request import GetUserRequest
from applications.user.get_user_response import GetUserResponse
from applications.user.create_user_request import CreateUserRequest
from applications.user.create_user_response import CreateUserResponse
from applications.user.update_user_request import UpdateUserRequest
from applications.user.update_user_response import UpdateUserResponse

from domains.user.user_repository import UserRepository
from domains.user.user_service import UserService
from domains.session.session_repository import SessionRepository
from domains.session.session_service import SessionService

from infrastructures.database import Database
from infrastructures.user.user_dto import UserDto, UserSchema
from infrastructures.session.session_dto import SessionDto


class TestUserApplicationService(TestCaseImpl):
    def test_コンストラクタ(self) -> None:
        user_repository = injector.get(UserRepository)
        user_service = injector.get(UserService)
        session_repository = injector.get(SessionRepository)
        session_service = injector.get(SessionService)
        user_application_service = UserApplicationService(
            user_repository, session_repository, user_service, session_service)
        assert user_application_service.user_repository == user_repository
        assert user_application_service.user_service == user_service
        assert user_application_service.session_repository == session_repository
        assert user_application_service.session_service == session_service


class TestGet(TestCaseImpl):
    def test_存在するAPIトークンとユーザIDを指定した場合正常なレスポンスを返す(self) -> None:
        user = self.db.session.query(UserDto).first()
        session = self.db.session.query(SessionDto).first()
        request = GetUserRequest(user.id, session.api_token)
        user_application_service = injector.get(UserApplicationService)
        response = user_application_service.get(request)
        assert isinstance(response, GetUserResponse)
        assert response.status == 200
        assert response.body()["id"] == str(user.id)
        assert response.body()["nickname"] == user.nickname
        assert response.body()["first_name"] == user.first_name
        assert response.body()["last_name"] == user.last_name
        assert response.body()["email"] == user.email
        assert response.body()["password"] == user.password

    def test_存在しないAPIトークンを指定した場合エラーを返す(self) -> None:
        user = self.db.session.query(UserDto).first()
        request = GetUserRequest(user.id, "")
        user_application_service = injector.get(UserApplicationService)
        response = user_application_service.get(request)
        assert isinstance(response, Error)
        assert response.status == 403
        assert response.message == "権限がありません。"

    def test_存在しないユーザIDを指定した場合エラーを返す(self) -> None:
        session = self.db.session.query(SessionDto).first()
        request = GetUserRequest(uuid4(), session.api_token)
        user_application_service = injector.get(UserApplicationService)
        response = user_application_service.get(request)
        assert isinstance(response, Error)
        assert response.status == 404
        assert response.message == "ユーザーは存在しません。"


class TestCreate(TestCaseImpl):
    def test_ユーザーを作成(self) -> None:
        request_body = {
            "nickname": "nickname",
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email@example.com",
            "password": "password"
        }
        request = CreateUserRequest(**request_body)
        user_application_service = injector.get(UserApplicationService)
        response = user_application_service.create(request)
        assert isinstance(response, CreateUserResponse)
        assert response.status == 201
        response_body = response.body()
        del response_body["id"]
        assert response_body == request_body

    def test_すでに存在するnicknameを指定した場合エラーを返す(self) -> None:
        user = self.db.session.query(UserDto).first()
        request_body = {
            "nickname": user.nickname,
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email@example.com",
            "password": "password"
        }
        request = CreateUserRequest(**request_body)
        user_application_service = injector.get(UserApplicationService)
        response = user_application_service.create(request)
        assert isinstance(response, Error)
        assert response.status == 409
        assert response.message == "そのニックネームはすでに使用されています。"

    def test_すでに存在するemailを指定した場合エラーを返す(self) -> None:
        user = self.db.session.query(UserDto).first()
        request_body = {
            "nickname": "nickname",
            "first_name": "first_name",
            "last_name": "last_name",
            "email": user.email,
            "password": "password"
        }
        request = CreateUserRequest(**request_body)
        user_application_service = injector.get(UserApplicationService)
        response = user_application_service.create(request)
        assert isinstance(response, Error)
        assert response.status == 409
        assert response.message == "そのメールアドレスはすでに登録されています。"


def get_user_from_db(db: Database) -> (dict, str):
    user = db.session.query(UserDto).first()
    session = db.session.query(
        SessionDto).filter_by(user_id=user.id).first()

    prev_user = UserSchema().dump(user)
    del prev_user["created_at"], prev_user["updated_at"]

    return prev_user, session.api_token


class TestUpdate(TestCaseImpl):
    def test_すべてのパラメータを指定してユーザ情報を更新(self) -> None:
        prev_user, api_token = get_user_from_db(self.db)
        request_body = {
            "nickname": "nickname",
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email@example.com",
            "password": "password"
        }
        request = UpdateUserRequest(api_token, prev_user["id"], **request_body)
        user_application_service = injector.get(UserApplicationService)
        response = user_application_service.update(request)
        assert isinstance(response, UpdateUserResponse)
        assert response.status == 201
        expected = request_body
        expected["id"] = prev_user["id"]
        assert response.body() == expected

    def test_api_tokenが無効の場合403エラー(self) -> None:
        prev_user, _ = get_user_from_db(self.db)
        request_body = {
            "nickname": "nickname",
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email@example.com",
            "password": "password"
        }
        request = UpdateUserRequest("", prev_user["id"], **request_body)
        user_application_service = injector.get(UserApplicationService)
        response = user_application_service.update(request)
        assert isinstance(response, Error)
        assert response.status == 403
        assert response.message == "権限がありません。"

    def test_他のユーザーのidを指定した場合403エラー(self) -> None:
        _, api_token = get_user_from_db(self.db)
        request_body = {
            "nickname": "nickname",
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email@example.com",
            "password": "password"
        }
        request = UpdateUserRequest(api_token, uuid4(), **request_body)
        user_application_service = injector.get(UserApplicationService)
        response = user_application_service.update(request)
        assert isinstance(response, Error)
        assert response.status == 403
        assert response.message == "ユーザーが一致しません。"

    def test_指定したnicknameがすでに使用されている場合409エラー(self) -> None:
        prev_user, api_token = get_user_from_db(self.db)
        other_user = self.db.session.query(
            UserDto).order_by(UserDto.id.desc()).first()
        request_body = {
            "nickname": other_user.nickname,
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email@example.com",
            "password": "password"
        }
        request = UpdateUserRequest(api_token, prev_user["id"], **request_body)
        user_application_service = injector.get(UserApplicationService)
        response = user_application_service.update(request)
        assert isinstance(response, Error)
        assert response.status == 409
        assert response.message == "そのニックネームはすでに使用されています。"

    def test_指定したemailがすでに使用されている場合409エラー(self) -> None:
        prev_user, api_token = get_user_from_db(self.db)
        other_user = self.db.session.query(
            UserDto).order_by(UserDto.id.desc()).first()
        request_body = {
            "nickname": "nickname",
            "first_name": "first_name",
            "last_name": "last_name",
            "email": other_user.email,
            "password": "password"
        }
        request = UpdateUserRequest(api_token, prev_user["id"], **request_body)
        user_application_service = injector.get(UserApplicationService)
        response = user_application_service.update(request)
        assert isinstance(response, Error)
        assert response.status == 409
        assert response.message == "そのメールアドレスはすでに登録されています。"
