import { User, UserDriver } from '@/domain/user'

export class UserDriverImpl implements UserDriver {
  constructor() {}

  create(user: User): User {
    return user
  }
}
