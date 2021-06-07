class SessionService:
    def __init__(self, user_repository, session_repository):
        self.user_repository = user_repository
        self.session_repository = session_repository

    def authenticated(self, cookie):
        return self.session_repository.find_by_cookie(cookie) is not None

    def find_user_by_cookie(self, cookie):
        session = self.session_repository.find_by_cookie(cookie)

        if session is None:
            return None

        user = self.user_repository.find_by_id(session.user_id)
        return user
