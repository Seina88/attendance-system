import { User } from '@/domain/user/user'

export type UserRepository = {
  create: (user: User) => User
}
