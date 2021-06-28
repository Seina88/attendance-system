import { User } from './user'

export type UserRepository = {
  create: (user: User) => User
}
