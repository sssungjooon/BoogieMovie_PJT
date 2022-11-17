<template>
  <div id="signup-page">
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>
      <br>
      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>
      <br>
      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      <br>
      <br>
      
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        // username,
        // password1,
        // password2,
        username: username,
        password1: password1,
        password2: password2,
      }

      this.$store.dispatch('signUp', payload)

    }
  }
}
</script>

<style>
#signup-page {
  background-image: url('https://s3-alpha-sig.figma.com/img/7029/d866/6a0bc64361956279c8e2ad111b7e1ee4?Expires=1669593600&Signature=dWzRumG~iEqwBLjwHyPBvzKr63REFXC1ejrym2PLHtqbCKFABmCSnmHkZe-lKZQ~f7EHqeXl74eEpKOTAgL39s2I4HIFIaznFnZZlgx8ENO1gEot7n9sA~TOR2HMjYI4wB7xKJOEx19dBxX~9ltt1jFeuYCg1RhcEvEq1oO-2Qva7zjZhFd1DdemukuATQaAU7p5SnA~9ABRGPS78gXieoqimdc1pmfVFFPpKOmzNIOYLoZRgzpn0dA6fk5csYBrPliZ6N9t5c27UtFAQDJ2sewKfVjgPZ-FFC~F5XKLZX8d9TR40ce~MOERFbfxA1nY6Ch4z0vQ-rJ75Kit6LXbTw__&Key-Pair-Id=APKAINTVSUGEWH5XD5UA');
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


</style>