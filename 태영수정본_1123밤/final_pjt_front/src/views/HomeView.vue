<template>
  <div class="home">
    <br><br><br>
    <h1>부귀영화</h1>
    <br>
    <MainPage/>
    <br>
    <TheSwiper :movies="latest_movies"/><br>
    <br>
    <h1>지금 뜨는 영화들</h1><br>
    <div>
      <MovieList :movies="latest_movies" />
    </div>
    <br>
    <hr>
    <br>
    <h1>높은 평점의 영화들</h1><br>
    <div>
      <MovieList :movies="highscore_movies" />
    </div>
    <br>
    <br>
    <br>
  </div>
</template>

<script>
// @ is an alias to /src
import MainPage from '@/components/MainPage.vue'
import MovieList from '@/components/MovieList.vue'
import TheSwiper from '@/components/TheSwiper.vue'
import axios from 'axios'

export default {
  name: 'HomeView',
  components: {
    MainPage,
    MovieList,
    TheSwiper,
  },
  data: function() {
    return {
      //selectedMovies: [],
      latest_movies : [],
      highscore_movies : [],
    }
  },
  // selected 메서드(알고리즘) 작성(MainRecommendVue참고)
  methods : {
    getLatestMovies : function(){
      const link2 = 'http://127.0.0.1:8000/movies/'
      axios.get(link2)
        .then(res =>{
          this.latest_movies = res.data.latest_movies
          this.highscore_movies = res.data.highscore_movies
          //this.like_movies = res.data.like_movies
        })
    }
  },
  created : function(){
    this.getLatestMovies()
  },
}
</script>

<style>
#home {
  /* background-image: url('https://s3-alpha-sig.figma.com/img/eac6/fc30/5b91075cabe3f0ba68d6c8fdd8c69bb8?Expires=1669593600&Signature=eGHwx0npSfqZ7emoGEdy1ispXLBTXPZA5XU9J7byjlcy987EfvwOgBCB~5lwmOHKxRWCpwzQNgFB-ED-kKiJiKfE9t1FmA3prOdfJuSOtlk1E3fQypeMyzie5j0iz2x6BTbC6sKWj1Y6ILyrTR~rt29wCLiBk5OtheqTIi1nO6~INKmFm7OuaE7FpReuZ-j-vI3xNB9I25n6YQ1GmADPTN9ikeDUI9wTAUa~hfS1AZu2EE7gZKgkpOFxZyft7tit1Qs2q243Q5eWs5Nh0UaFcav7gRdwD4u~M-Jli43YutQcqYSjXu0SrnmEF0crsvU4fjfY~Q1lIatHXdwe~jstQA__&Key-Pair-Id=APKAINTVSUGEWH5XD5UA'); */
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