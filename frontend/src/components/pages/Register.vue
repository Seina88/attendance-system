<template>
  <div class="register">
    <div class="card">
      <header class="register_header">
        <h2>Create New User</h2>
      </header>
      <div class="content">
        <form action="" class="register_form">
          <dl>
            <dt class="user_name">User Name</dt>
            <dd>
              <input
                type="text"
                name="user_name"
                placeholder="User Name"
                id="user_name"
                v-model="nickname"
                required
              />
            </dd>
            <dt class="first_name">First Name</dt>
            <dd>
              <input
                type="text"
                name="first_name"
                placeholder="First Name"
                id="first_name"
                v-model="firstName"
                required
              />
            </dd>
            <dt class="last_name">Last Name</dt>
            <dd>
              <input
                type="text"
                name="last_name"
                placeholder="Last Name"
                id="last_name"
                v-model="lastName"
                required
              />
            </dd>
            <dt class="mail_address">Mail Address</dt>
            <dd>
              <input
                type="text"
                name="mail_address"
                placeholder="Mail Address"
                id="mail_address"
                v-model="email"
                required
              />
            </dd>
            <dt class="password">Password</dt>
            <dd>
              <input
                type="text"
                name="password"
                placeholder="Password"
                id="password"
                v-model="password"
                required
              />
            </dd>
          </dl>
          <div class="submit">
            <input class="button" type="submit" name="submit" value="Sign Up" />
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data () {
    return {
      nickname: '',
      firstName: '',
      lastName: '',
      email: '',
      password: ''
    }
  }
}
</script>

<style scoped>
.register {
  width: 100%;
  height: 100%;
  background: #c0c0c0;
  display: flex;
  align-items: center;
  justify-content: center;
}
.card {
  width: 400px;
}
.register_header {
  background-color: #ffb6b9;
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  color: #fff;
  height: 88px;
  display: flex;
  align-items: center;
  justify-content: center;
}
h2 {
  font-size: 28px;
}
.content {
  background-color: #fff;
  border-bottom-left-radius: 20px;
  border-bottom-right-radius: 20px;
  color: #777;
  padding: 24px 28px;
  height: 300px;
}
form dl {
  margin: 0 auto;
}
form dl dt {
  width: 120px;
  padding: 8px;
  float: left;
  clear: both;
}
form dl dd {
  padding: 8px 0;
}
form dl dd input {
  width: 60%;
  height: 22px;
  padding: 1px 4px;
}
input::placeholder {
  color: #c0c0c0;
}
.register_form input[type=text] {
  background-color: #eee;
  color: #777;
  border: none;
}
.button {
  display: block;
  margin: 0 auto;
  margin-top: 32px;
  background-color: #bbded6;
  color: #fff;
  padding: 8px 16px;
  border: none;
}
.button:focus,
.button:hover {
  background-color: #61c0bf;
}
</style>
