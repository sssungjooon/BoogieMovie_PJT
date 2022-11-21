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
      isLoggedIn : true
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
  background-image: url('https://s3-alpha-sig.figma.com/img/eac6/fc30/5b91075cabe3f0ba68d6c8fdd8c69bb8?Expires=1669593600&Signature=eGHwx0npSfqZ7emoGEdy1ispXLBTXPZA5XU9J7byjlcy987EfvwOgBCB~5lwmOHKxRWCpwzQNgFB-ED-kKiJiKfE9t1FmA3prOdfJuSOtlk1E3fQypeMyzie5j0iz2x6BTbC6sKWj1Y6ILyrTR~rt29wCLiBk5OtheqTIi1nO6~INKmFm7OuaE7FpReuZ-j-vI3xNB9I25n6YQ1GmADPTN9ikeDUI9wTAUa~hfS1AZu2EE7gZKgkpOFxZyft7tit1Qs2q243Q5eWs5Nh0UaFcav7gRdwD4u~M-Jli43YutQcqYSjXu0SrnmEF0crsvU4fjfY~Q1lIatHXdwe~jstQA__&Key-Pair-Id=APKAINTVSUGEWH5XD5UA');
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

body {
  margin: 0;
}

.navbar-box {
  background-color: rgb(11, 18, 36);
}

.nav-bar {
  width: 100%;
  background-size: 100vw;
  /* 배경 바뀌는거 알아보기... */
  text-align: right;
  color: white;
  text-decoration-color: white;
  
}

</style>

