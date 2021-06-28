import { User, UserDriver, UserRepository } from '@/domain/user'

export class UserRepositoryImpl implements UserRepository {
  private userDriver: UserDriver

  constructor(userDriver: UserDriver) {
    this.userDriver = userDriver
  }

  create(user: User): User {
    return this.userDriver.create(user)
  }
}
