import { User } from './user'

export type UserDriver = {
  create: (user: User) => User
}
