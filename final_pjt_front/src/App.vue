<template>
  <div id="app">
    <div class="navbar-box" style="width: 100%;">
      <nav class="nav-bar">
        <span>
          <router-link style="text-decoration:none; color: white;" :to="{name:'home'}">Home</router-link> |
          <router-link style="text-decoration:none; color: white;" :to="{name:'recommended'}">Recommend</router-link> |
          <!-- <router-link style="text-decoration:none; color: white;" :to="{name:'signup'}">SignUp</router-link> | -->
          <router-link v-if="isLoggedIn" @click="logout" style="text-decoration:none; color: white;" :to="{name:'home'}">Logout</router-link>
          <router-link v-else type="button" style="text-decoration:none; color: white;" :to="{name:'login'}">LogIn</router-link> |
          <router-link style="text-decoration:none; color: white;" :to="{name:'mypage'}">MyPage</router-link>
        </span>
      </nav>
    </div>
    <router-view/>
  </div>
</template>

<script>

 
export default {
  name: 'App',
  components: {
    
  },
  data() {
    // 로그인 정보 담아오기
    return {
      isLoggedIn : false
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
    }
  }
}
</script>

<style>
#app {
  background-image: url('./assets/backgroundimage1.jpeg');
  background-size:cover;
  width: 100%;
  height:100%;
  margin: 0;
  padding: 0;
  position:static;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
}

body {
  margin: 0;
}

.navbar-box {
  background-color: rgb(11, 18, 36);
  position: fixed;
  top:0;
  z-index: 1;
}

.nav-bar {
  width: 100%;
  background-size: 100vw;
  /* 배경 바뀌는거 알아보기... */
  text-align: right;
  color: white;
  text-decoration-color: white;
  
}

@font-face {
  font-family: 'samlip';
  src: url(./fonts/SDSamliphopangcheTTFOutline.ttf) format('woff');
  font-weight: normal;
  font-style: normal;
}

</style>

