<template>
  <div id="signup-page">
    <br><br>
    <h1>Sign Up Page</h1><br>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input class="signup-input" type="text" id="username" v-model="username"><br>
      <br>
      <label for="password1"> password : </label>
      <input class="signup-input" type="password" id="password1" v-model="password1"><br>
      <br>
      <label for="password2"> password confirmation : </label>
      <input class="signup-input" type="password" id="password2" v-model="password2">
      <br>
      <br>
      <div id="genre-box">
        <h4 class="choose-text">Choose your favorite genres</h4>
        <div class="genre-buttons">
          <button @click="onSelectGenre" class="raise" data-id="878">SF</button>
          <button @click="onSelectGenre" class="raise" data-id="10770">TV영화</button>
          <button @click="onSelectGenre" class="raise" data-id="10751">가족</button>
          <button @click="onSelectGenre" class="raise" data-id="27">공포</button>
          <button @click="onSelectGenre" class="raise" data-id="99">다큐멘터리</button>
          <button @click="onSelectGenre" class="raise" data-id="18">드라마</button>
          <button @click="onSelectGenre" class="raise" data-id="10749">로맨스</button>
          <button @click="onSelectGenre" class="raise" data-id="12">모험</button>
          <button @click="onSelectGenre" class="raise" data-id="9648">미스터리</button>
          <button @click="onSelectGenre" class="raise" data-id="80">범죄</button>
          <button @click="onSelectGenre" class="raise" data-id="37">서부</button>
          <button @click="onSelectGenre" class="raise" data-id="53">스릴러</button>
          <button @click="onSelectGenre" class="raise" data-id="16">애니메이션</button>
          <button @click="onSelectGenre" class="raise" data-id="28">액션</button>
          <button @click="onSelectGenre" class="raise" data-id="36">역사</button>
          <button @click="onSelectGenre" class="raise" data-id="10402">음악</button>
          <button @click="onSelectGenre" class="raise" data-id="10752">전쟁</button>
          <button @click="onSelectGenre" class="raise" data-id="35">코미디</button>
          <button @click="onSelectGenre" class="raise" data-id="14">판타지</button>
        </div>
      </div>
      <br>      
      <input class="signup-button" type="submit" value="SignUp">
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

    },
    onSelectGenre: function (event) {
      const genreId = event.target.dataset.id
      const genreBtn = event.target
      if (!genreBtn.classList.contains('raise-focus')) {
        genreBtn.classList.add('raise-focus')
        this.payload.genres.push(genreId)
      } else {
        genreBtn.classList.remove('raise-focus')
        const idx = this.payload.genres.indexOf(genreId)
        this.payload.genres.splice(idx, 1)
      }
    }
  }
}
</script>

<style>
#signup-page {
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
  /* opacity: 0.5; */
}
.genre-buttons .raise:hover,
.genre-buttons .raise-focus {
  font-size: 0.75rem;
  box-shadow: 0 0.5em 0.5em -0.4em #b10101;
  border: 2px solid #b10107a1;
  transform: translateY(-0.25em);
  background-color: #5a051438;
  font-weight: bold;
  color: #87070dec;
  transition: all .5s;
}
.genre-buttons button {
  width: 5rem;
  background: none;
  border: 2px solid;
  font: inherit;
  line-height: 1;
  margin: 0.5em;
  padding: 0.5em;
  color: white;
  font-size: 0.75rem;
  transition: all .5s;
}

.signup-button:hover {
  background-color: rgb(75, 4, 20);
  transition: all .5s;
  transform: translateY(-0.25em);

}
.signup-button-focus {
  font-size: 0.9rem;
  border: 2px solid #290693a1;
  background-color: #0f1cae38;
  font-weight: bold;
  color: #240372ec;
  transition: all .5s;
}
.signup-button {
  width: 5rem;
  background-color: white;
  border: 2px solid black;
  line-height: 2;
  font: inherit;
  font-style: bold;
  color: black;
  font-size: 0.9rem;
  margin: 0.5em;
  padding: 0.5em;
  font-weight: bold;
}
.signup-input {
  background-color: black;
  color:white;
  border: 1px solid white;

}
#genre-box {
  width: 80%;
  justify-content: center;
  margin: auto;
}
</style>