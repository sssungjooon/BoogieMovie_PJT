<template>
  <div id="app">
    <div class="navbar-box" style="width: 100%;">
      <nav class="nav-bar">
        <span>
          <router-link class="router" style="text-decoration:none; color: white;" :to="{name:'home'}">Home</router-link> |
          <router-link class="router" style="text-decoration:none; color: white;" :to="{name:'recommended'}">Recommend</router-link> 
          <!-- <router-link style="text-decoration:none; color: white;" :to="{name:'signup'}">SignUp</router-link> | -->
          <!-- <router-link v-if="isLogin" @click="logout" style="text-decoration:none; color: white;" :to="{name:'home'}">Logout</router-link> -->
          <router-link class="router" v-if="!isLogin" type="button" style="text-decoration:none; color: white;" :to="{name:'login'}">LogIn</router-link> |
          <a id="logout" class="router" v-if="isLogin" style="text-decoration:none; color: white;" href="#" @click="logout">Logout | </a>
          <router-link class="router" style="text-decoration:none; color: white;" :to="{name:'mypage'}">MyPage</router-link>
        </span>
      </nav>
    </div>
    <router-view class="router-view"/>
  </div>
</template>

<script>
//import store from '@/store/index.js'
 
export default {
  name: 'App',
  components: {
    
  },
  // data() {
  //   // 로그인 정보 담아오기
  //   return {
  //     isLoggedIn : store.state.token
  //   }
  // },
  methods: {
    logout() {
      this.$store.commit('LOG_OUT')
      //console.log('12364')
      //this.$store.dispatch('logout')
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },

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
  font-family: samlip;
}

body {
  margin: 0;
}

.navbar-box {
  background-color: rgb(11, 18, 36);
  position: fixed;
  top:0;
  z-index: 10;
}

.router-view {
  z-index: 3;
}
span.router:hover {
  background-color: rgb(57, 197, 204);
  transition: all .5s;
  transform: translateY(-0.25em);
  color: rgb(7, 7, 0);
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

