from ..models.session_model import SessionModel


class SessionRepository:
    def __init__(self, database, model=SessionModel):
        self.database = database
        self.session = database.session
        self.model = model

    def find_by_cookie(self, cookie):
        return self.session.query(self.model).filter_by(cookie=cookie).first()

    def add(self, session):
        self.session.add(session)

    def commit(self):
        self.session.commit()
