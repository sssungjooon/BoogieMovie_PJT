<template>
  <div class="home">
    <p>123</p>
    <FirstComponent/>
    <br>
    <div>
      <MovieList :movies="selectedMovies" />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import FirstComponent from '@/components/FirstComponent.vue'
import MovieList from '@/components/MovieList.vue'
export default {
  name: 'HomeView',
  components: {
    FirstComponent,
    MovieList,
  },
  data: function() {
    return {
      selectedMovies: [],

    }
  },
  // selected 메서드(알고리즘) 작성(MainRecommendVue참고)
}
</script>

<style>
#home {
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
}</style>