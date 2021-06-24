<template>
    <div class="login">
      <div class="card">
        <header class="login_header">
          <h2>
            Sign In
          </h2>
        </header>
        <div class="content">
          <form class="login_form">
            <div class="login_info">
              <label for="info">User Name / Email</label>
                <input
                  type="text"
                  name="info"
                  placeholder="UserName / Email"
                  id="info"
                  v-model="info"
                  required
                >
            </div>
            <div class="login_password">
              <label for="password">Password</label>
                <input
                  :type="showPassword ? 'text' : 'password'"
                  name="password"
                  class="input-password"
                  placeholder="password"
                  id="password"
                  v-model="password"
                  required
                >
                <span class="eye-icon">
                  <img :src="eyeImage" @click="showPassword = !showPassword">
                </span>
            </div>
            <div class="submit">
              <input class="button" type="submit" value="Sign In">
            </div>
            <div class="create_user">
              <button class="button" type="create_user" @click="createUser">Create User</button>
            </div>
          </form>
        </div>
      </div>
    </div>
</template>

<script>
import eyeOpenImage from '@/assets/img/eye.png'
import eyeCloseImage from '@/assets/img/eye-off.png'

export default {
  name: 'Login',
  data: function () {
    return {
      info: '',
      password: ''
    }
  },
  computed: {
    eyeImage: function () {
      return this.showPassword ? eyeCloseImage : eyeOpenImage
    }
  },
  methods: {
    createUser: function () {
      this.$router.push('/register')
    }
  }
}
</script>

<style scoped>
.input-password{
  display: inline;
  padding-right: 30px;
}
.login {
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
.login_header {
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
  font-size: 35px;
}
.content {
  background-color: #fff;
  border-bottom-left-radius: 20px;
  border-bottom-right-radius: 20px;
  color: #777;
  display: grid;
  padding: 20px 28px;
  height: 280px;
}
.login_password {
  position: relative;
  margin-top: 10px;
}
.eye-icon {
  position: absolute;
  right: 8px;
  top: 34px;
  cursor: pointer;
}
.login input[type="password"],
.login input[type="text"] {
  background-color: #eee;
  color: #777;
  padding: 4px;
  width: calc(100% - 8px);
  font-size: 16px;
  height: 32px;
}
.login input[type="password"]::placeholder,
.login input[type="text"]::placeholder {
  color: #c0c0c0;
}
.submit {
  margin-top: 40px;
}
input {
  background-image: none;
  border: none;
  font: inherit;
  margin: 0;
  padding: 0;
  transition: all 0.3s;
}

/* ---------- BUTTON ---------- */
.button[type="submit"] {
  background-color: #bbded6;
  color: #fff;
  padding: 0.25em 1.5em;
  display: block;
  margin: 0 auto;
  width: 100%;
}
.button:focus[type="submit"],
.button:hover[type="submit"] {
  background-color: #61c0bf;
}
.button[type="create_user"] {
  color: #c0c0c0;
  background: #fff;
  border: 0.05px solid;
  font-size: 12px;
  padding: 0.25em 1.5em;
  display: block;
  margin: 32px auto;
  text-align:center;
}
.button:focus[type="create_user"],
.button:hover[type="create_user"] {
  color: #8a8787;
}
</style>
