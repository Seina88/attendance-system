import { User } from './user'

export type UserUseCase = {
  create: (user: User) => User
}
