<template>
  <div>
    <br>
    <h1>Movies for you</h1>
    <br>
    <div class="recommend-movies">
      <h3>다가오는 크리스마스에는 이런 영화 어때요?</h3>
      <br>
      <div>
        <MovieList :movies="christmas_movies" />
      </div>
      <br>
      <hr>
      <br>
      <h3>2021년도에는 이런 영화가?</h3>
      <br>
      <div>
        <MovieList :movies="datetime_movies" />
      </div>
      <br>
      <hr>
      <br>
      <h3>다가오는 크리스마스에는 이런 영화 어때요?</h3>
      <br>
      <div>
        <MovieList :movies="christmas_movies" />
      </div>
      <br>
      <br>
      <br>
    </div>
    

  </div>
</template>

<script>
import MovieList from '@/components/MovieList'
import axios from 'axios'

export default {
  name: 'RecommendedView',
  components: {
    MovieList,
  },
  data: function() {
    return {
      //selectedMovies: [],
      christmas_movies : [],
      datetime_movies : [],
    }
  },
  methods : {
    getRecommendMovies : function(){
      const link3 = 'http://127.0.0.1:8000/movies/recommend'
      axios.get(link3)
        .then(res =>{
          this.christmas_movies = res.data.christmas_movies
          this.datetime_movies = res.data.datetime_movies
          //this.highscore_movies = res.data.highscore_movies
          //this.like_movies = res.data.like_movies
        })
    }
  },
  created : function(){
    this.getRecommendMovies()
  },
}
</script>
      

<style>

.recommend-movies {
  text-align: left;
  margin: 2rem;
}

</style>