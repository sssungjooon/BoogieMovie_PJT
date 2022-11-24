<template>
  <div>
    <br><br><br>
    <h1>Movies for you</h1>
    <h1>당신을 위한 영화</h1>
    <hr>
    <br>
    <div class="recommend-movies">
      <div class="content1">
        <img src="@/assets/christmas-tree.jpg" class="tree"/><h3 class = "text1">다가오는 크리스마스에는 이런 영화 어때요?</h3><img src="@/assets/christmas-tree.jpg" class="tree"/>
      </div>
      <br>
      <div>
        <MovieList :movies="christmas_movies" />
      </div>
      <br>
      <hr>
      <br>
      <h3>2010년 대에는 이런 영화가?</h3>
      <br>
      <div>
        <MovieList :movies="datetime_movies" />
      </div>
      <br>
      <hr>
      <br>
      <div class="content1">
        <img src="@/assets/spiderman.png" class="spider"/><h3>히어로 영화 좋아하는 사람은 여기로!</h3><img src="@/assets/spiderman.png" class="spider"/>
      </div>
      <br>
      <div>
        <MovieList :movies="hero_movies" />
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
      hero_movies : [],
    }
  },
  methods : {
    getRecommendMovies : function(){
      const link3 = 'http://127.0.0.1:8000/movies/recommend'
      axios.get(link3)
        .then(res =>{
          this.christmas_movies = res.data.christmas_movies
          this.datetime_movies = res.data.datetime_movies
          this.hero_movies = res.data.hero_movies
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

.tree {
  width: 30px;
  height: 30px;
  }

.spider {
  width: 30px;
  height: 30px;
}

.content1{
    display: flex;
    align-items: center;
}


</style>