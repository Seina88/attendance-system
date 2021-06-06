from ..models.user_model import UserModel


class UserRepository:
    def __init__(self, database, model=UserModel):
        self.database = database
        self.model = model

    def get_all(self):
        return self.database.session.query(self.model).all()

    def get_by_id(self, id):
        return self.database.session.query(self.model).filter_by(id=id).first()

    def get_by_email(self, email):
        return self.database.session.query(self.model).filter_by(email=email).all()

    def add(self, user):
        self.database.session.add(user)

    def commit(self):
        self.database.session.commit()
