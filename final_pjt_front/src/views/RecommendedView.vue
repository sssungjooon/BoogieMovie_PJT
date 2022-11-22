<template>
  <div>
    <br>
    <h1>Movies for you</h1>
    <br>
    <div class="recommend-movies">
      <h3>다가오는 크리스마스에는 이런 영화 어때요?</h3>
      <br>
      <MovieList/>
    </div>
    

  </div>
</template>

<script>
import MovieList from '@/components/MovieList'

export default {
  name: 'RecommendedView',
  components: MovieList,
}
</script>

<style>

.recommend-movies {
  text-align: left;
  margin: 2rem;
}

</style>