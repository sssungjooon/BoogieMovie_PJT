<template>
  <div id="login-page">
    <br><br>
    <h1>Login Page</h1>
    <form @submit.prevent="logIn">
      <label for="username">username : </label>
      <input class="login-input" type="text" id="username" v-model="username"><br>
      <br>
      <label for="password"> password : </label>
      <input class="login-input" type="password" id="password" v-model="password"><br>
      <br>
      <input class="login-button" type="submit" value="logIn">
    </form>
    <hr>
    <h5>아직 아이디가 없으신가요?</h5>
    <br>
    <router-link id="signup-button2"  :to="{name:'signup'}">회원가입</router-link>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    }
  }
}
</script>

<style>

#login-page {
  background-image: url('@/assets/backgroundimage2.jpeg');
  background-size: 100vw 100vh;
  width: 100%;
  height:100vh;
  margin: 0;
  padding: 0;
  position: absolute;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
}

.login-button {
  width: 5rem;
  background-color: white;
  border: 2px solid black;
  line-height: 1;
  font: inherit;
  font-style: bold;
  color: black;
  font-size: 0.9rem;
  margin: 0.2em;
  padding: 0.2em;
  font-weight: bold;
}

.login-input{
  background-color: black;
  color:white;
  border: 1px solid white;
}
.login-button:hover {
  background-color: rgb(75, 4, 20);
  transition: all .5s;
  transform: translateY(-0.25em);

}
#signup-button2 {
  width: 50px;
  background-color: white;
  border: 2px solid black;
  line-height: 1;
  font: inherit;
  font-style: bold;
  color: black;
  font-size: 0.9rem;
  margin: 2em;
  padding: 0.4em;
  font-weight: bold;
  text-decoration: none;
}
#signup-button2:hover {
  background-color: rgb(75, 4, 20);
  transition: all .5s;
  transform: translateY(-0.25em);

}
</style>