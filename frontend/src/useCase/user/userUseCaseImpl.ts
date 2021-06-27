import { User, UserRepository, UserUseCase } from '@/domain/user'

export class UserUseCaseImpl implements UserUseCase {
  private userRepository: UserRepository

  constructor(userRepository: UserRepository) {
    this.userRepository = userRepository
  }

  create(user: User): User {
    return this.userRepository.create(user)
  }
}
