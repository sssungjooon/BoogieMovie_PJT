<template>
  <div class="movie-info-section">
    <div class="trailer-container">
      <iframe :src="videoUrl" frameborder="0"></iframe>
    </div>
    <section class="information-container">
        <h2 class="movie-title">{{ movieName }}</h2>
        <h4 class="movie-date">{{ movieDate }}</h4>
        <div class="transformers-right">
          <StarRating :rating="parseFloat(movieVote) / 2" :read-only="true" :increment="0.01"/>
        </div>
        <div class="score-like-button-box">
          <!-- <h2 class="movie-score">{{ movieVote }}</h2>           -->
          <h2 class="movie-button">
              <i class="fa-solid fa-heart-circle-plus" id="movie-normal-button" v-if='normal' @click='movielike(), normal=false, like=true'/>
              <i class="fa-solid fa-heart-circle-check" id="movie-like-button" v-if='like' @click='movielike(), like=false, dislike=true'/>
              <i class="fa-solid fa-heart-circle-xmark" id="movie-dislike-button" v-if='dislike' @click='movielike(), dislike=false, normal=true'/>
          </h2>         
        </div>
    </section>
    <div class="overview-container">
      {{ movieOverview }}
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
// import drf from '@/api/drf'
import { mapGetters } from 'vuex'
// import secret_data from "@/assets/secrets.json"
import StarRating from 'vue-star-rating'

export default {
  name: "MovieDetailInfoSection",
  props: {
    movieId: Number,
    movieName: String,
    movieVideo: String,
    movieOverview: String,
    movieVote: Number,
    movieDate: Date,
  },
  components: {
    StarRating,
  },
  data: function () {
    return {
      trailerURL: '',
      movie: {},
      like: false,
      dislike: false,
      normal: false,
    }
  },
  // methods: {
  //   movielike () {
  //     axios({
  //       url: drf.movies.likeMovie(this.movieId),
  //       method: 'post',
  //       headers: this.authHeader
  //     })
  //   },
  // },
    computed : {
      videoUrl() {
        const videoId = this.movieVideo
        const VIDEO_URL = `https://www.youtube.com/embed/${videoId}`
        return VIDEO_URL
      },
      ...mapGetters(['authHeader'])
    },
  // created () {
  //   const tmdbAPI = secret_data.TMDB_API_KEY
  //   const youtubeAPI = secret_data.YOUTUBE_API_KEY
  //   axios({
  //     url: `https://api.themoviedb.org/3/movie/${this.movieId}/videos`,
  //     method: 'get',
  //     params: {
  //       'api_key': tmdbAPI,
  //       'region': 'KR',
  //       'language': 'ko',
  //     }
  //   })
  //   .then(res => {
  //     if (res.data.results[0]) {
  //       this.trailerURL = 'https://www.youtube.com/embed/' + res.data.results[0]['key']
  //     }
  //     else {
  //       const API_KEY = youtubeAPI
  //       const API_URL = 'https://www.googleapis.com/youtube/v3/search'
  //       const params = {
  //         key: API_KEY,
  //         part: 'snippet',
  //         q: this.movieName,
  //         type: 'video',
  //       }
  //       axios.get(API_URL, {params,})
  //       .then(res => {
  //         const selected = res.data.items[0]
  //         this.trailerURL = `https://www.youtube.com/embed/${selected.id.videoId}`
  //       })
  //     }
  //   })

  //   axios({
  //     url: drf.movies.movie(this.movieId),
  //     method: 'get',
  //   })
  //   .then(res => {
  //     this.movie = res.data
  //     axios({
  //       url: drf.accounts.currentUserInfo(),
  //       method: 'get',
  //       headers: this.authHeader
  //     })
  //     .then(res => {
  //       const userId = res.data.pk
  //       const like_users = this.movie.like_users
  //       const dislike_users = this.movie.dislike_users
  //       if (like_users.includes(userId)) {
  //         this.like = true
  //       } else if (dislike_users.includes(userId)) {
  //         this.dislike = true
  //       } else {
  //         this.normal = true
  //       }
  //     })
  //   })
  // }
}
</script>

<style>

.movie-info-section {
  margin: 1rem;
}

.trailer-container {
  position: relative;
  padding-top: 50%;
}

.trailer-container > iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%
}

.information-container  {
  display: flex;
  justify-content: space-between;
  margin-top: 1rem;
}

.movie-title {
  text-align: left;
  color: white;
  font-weight: bold;
}

.score-like-button-box {
  display: flex;
}

.movie-score {
  color: white;
  font-weight: bold;
  margin-right: 1rem;
}

#movie-normal-button {
  text-align: center;
  color: white;
  animation: neon1 1.5s ease-in-out infinite alternate;
}

#movie-like-button {
  text-align: center;
  color: crimson;
  animation: neon2 1.5s ease-in-out infinite alternate;
}

#movie-dislike-button {
  text-align: center;
  color: rgb(46, 46, 46);
  animation: neon3 1.5s ease-in-out infinite alternate;
}

@keyframes neon1 {
  from {
    text-shadow: 0 0 2px rgba(255, 255, 255, 0.575), 0 0 4px rgba(255, 255, 255, 0.671), 0 0 6px rgba(255, 255, 255, 0.726), 0 0 8px #00adb9,
      0 0 10px #0066aa, 0 0 12px #bd0153, 0 0 14px #4c00c7, 0 0 16px #00adb9;
  }
  to {
    text-shadow: 0 0 5px rgba(255, 255, 255, 0.747), 0 0 10px rgba(255, 255, 255, 0.651), 0 0 15px rgba(255, 255, 255, 0.644), 0 0 20px #00adb9,
      0 0 35px #0066aa, 0 0 40px #bd0153, 0 0 50px #4c00c7, 0 0 75px #00adb9;
  }
}

@keyframes neon2 {
  from {
    text-shadow: 0 0 2px rgba(255, 124, 174, 0.616), 0 0 4px rgba(255, 124, 174, 0.616), 0 0 6px rgba(255, 124, 174, 0.616), 0 0 8px #c5009473,
      0 0 10px #c40142, 0 0 12px #bd0153, 0 0 14px #e000c2, 0 0 16px #dd00009a;
  }
  to {
    text-shadow: 0 0 5px rgba(255, 255, 255, 0.747), 0 0 10px rgba(255, 255, 255, 0.651), 0 0 15px rgba(255, 255, 255, 0.644), 0 0 20px #c5009473,
      0 0 35px #c40142, 0 0 40px #bd0153, 0 0 50px #e000c2, 0 0 75px #dd00009a;
  }
}

@keyframes neon3 {
  from {
    text-shadow: 0 0 2px rgba(121, 121, 121, 0.616), 0 0 4px rgba(121, 121, 121, 0.616), 0 0 6px rgba(121, 121, 121, 0.616), 0 0 8px #585858ab,
      0 0 10px #4f0074, 0 0 12px #150c63, 0 0 14px #155468, 0 0 16px #1b6a7ee1;
  }
  to {
    text-shadow: 0 0 5px rgba(121, 121, 121, 0.616), 0 0 10px rgba(121, 121, 121, 0.616), 0 0 15px rgba(121, 121, 121, 0.616), 0 0 20px #585858ab,
      0 0 35px #4f0074, 0 0 40px #150c63, 0 0 50px #155468, 0 0 75px #1b6a7ee1;
  }
}

.movie-score {
  position: relative;
}

.overview-container {
  margin-top: 1rem;
  text-align: left;
  color: white;
}

</style>