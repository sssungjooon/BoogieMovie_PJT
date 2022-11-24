<template>
  <div>
    <hr><br>
    <p style="font-size:20px;">내가 좋아하는 영화</p>
    <MovieList :movies="liked_movies" />
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'
import axios from 'axios'
export default {
  name: 'LikedMovieView',
  components: {
    MovieList,
  },
  data : function() {
    return {
        liked_movies : [],
    }
  },
  methods : {
    getLikedMovies : function(){
      const link2 = 'http://127.0.0.1:8000/movies/'
      axios.get(link2)
        .then(res =>{
          this.liked_movies = res.data.liked_movies
        })
    }
  },
  created : function(){
    this.getLikedMovies()
  },
}
</script>

<style>

</style>