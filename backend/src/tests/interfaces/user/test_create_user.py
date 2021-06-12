import json
from uuid import UUID

from tests.main_test_case import MainTestCase


class TestCreateUser(MainTestCase):
    def test_ユーザを作成(self) -> None:
        request = {
            "nickname": "nickname",
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email@example.com",
            "password": "password"
        }
        response = self.client.post(
            "/api/users/create", data=json.dumps(request), content_type="application/json"
        )
        data = json.loads(response.data)
        self.assert_status(response, 201)
        assert isinstance(UUID(data["id"]), UUID)
        request["id"] = data["id"]
        assert data == request
