from ..models.user_model import UserModel


class UserRepository:
    def __init__(self, database, model=UserModel):
        self.database = database
        self.session = database.session
        self.model = model

    def find_all(self):
        return self.session.query(self.model).all()

    def find_by_id(self, id):
        return self.session.query(self.model).filter_by(id=id).first()

    def find_by_nickname(self, nickname):
        return self.session.query(self.model).filter_by(nickname=nickname).first()

    def find_by_email(self, email):
        return self.session.query(self.model).filter_by(email=email).first()

    def add(self, user):
        self.session.add(user)

    def commit(self):
        self.session.commit()
