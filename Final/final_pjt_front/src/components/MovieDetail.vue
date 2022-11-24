<template>
  <div>
    <section id="movie-detail-section">
      <div id="detail-info-flex">
        <MovieDetailInfo :movieId="movieId" :movieName="movieName" :movieVideo="movieVideo" :movieOverview="movieOverview" :movieVote="movieVote" :movieDate="movieDate"/>
      </div>
      <!-- <div id="review-flex">
        <MovieDetailReview :movieId="movieId" />
      </div> -->
      <div id="add-flex">
        <!-- 배우/키워드 작성해보기 -->
        <MovieDetailAdd :movieActor="movieActor" :movieGenre="movieGenre" class="more"/>
      </div>
    </section>
  </div>
</template>

<script>
import MovieDetailInfo from "@/components/MovieDetailInfo.vue"
import MovieDetailAdd from '@/components/MovieDetailAdd.vue'
// import MovieDetailReview from "@/components/MovieDetailReview.vue"

export default {
  props: {
    movieId: Number,
    movieName: String,
    movieVideo: String,
    movieOverview: String,
    movieVote: Number,
    movieDate: String,
    movieActor: Array,
    movieGenre: Array,
  },
  components: {
    MovieDetailInfo,
    // MovieDetailReview,
    MovieDetailAdd,
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

#add-flex {
  width:28%;
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