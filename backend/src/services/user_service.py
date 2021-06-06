class UserService:
    def __init__(self, repository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id):
        return self.repository.get_by_id(id)

    def exists(self, user):
        users_having_the_same_email = self.repository.get_by_email(user.email)
        return len(users_having_the_same_email) > 0

    def add(self, user):
        self.repository.add(user)
        self.repository.commit()
