<template>
  <div>
    <section id="movie-detail-section">
      <div id="detail-info-flex">
        <MovieDetailInfoSection :movieId="movieId" :movieName="movieName"/>
      </div>
      <div id="review-flex">
        <MovieDetailReview :movieId="movieId" />
      </div>
    </section>
  </div>
</template>

<script>
import MovieDetailInfoSection from "@/components/MovieDetailInfoSection.vue"
import MovieDetailReview from "@/components/MovieDetailReview.vue"

export default {
  props: {
    movieId: Number,
    movieName: String,
  },
  components: {
    MovieDetailInfoSection,
    MovieDetailReview,
  },
}
</script>

<style>
#movie-detail-section {
  display: flex;
  flex-direction: row;
}

#detail-info-flex {
  width: 70%;
}

#review-flex {
  width: 30%;
  transition: 0.5s;
}

@media ( max-width: 1400px ) {
  #detail-info-flex {
    width: 100%;
  }

  #review-flex {
    width: 100%;
    transition: 0.5s;
  }

  #movie-detail-section {
    display: flex;
    flex-direction: column;
  }
}

</style>