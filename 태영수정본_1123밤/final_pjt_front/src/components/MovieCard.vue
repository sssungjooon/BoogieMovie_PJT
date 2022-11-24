<template>
 <div class="col">
  <ModalView v-if="isModalViewed" @close-modal="isModalViewed=false">
    <MovieDetail :movieId="movie.id || movie.tmdb_movie_id" :movieName="movie.title || movie.name" :movieVideo="movie.video_path" :movieOverview="movie.overview" :movieVote="movie.vote_average" :movieDate="movie.release_date"/>
  </ModalView>
  <div class="flip-card" @click="isModalViewed=true, showModal()">
    <div class="card-front">
      <figure>
        <div class="img-bg"></div>
        <img :src="posterPath" />
      </figure>
    </div>

    <div class="card-back">
      <figure>
        <div class="img-bg"></div>
        <img :src="posterPath" />
      </figure>

      <ul class="card-ul">
        <li>{{ movie.title || movie.name }}</li>
        <div class="transformers-right">
          <StarRating :rating="parseFloat(movie.vote_average) / 2" :read-only="true" :increment="0.01"/>
        </div>
        <!-- <div class="star-box">
          <i :id="idPath" data-id="1" class="fa-solid fa-star"></i>
          <i :id="idPath" data-id="2" class="fa-solid fa-star"></i>
          <i :id="idPath" data-id="3" class="fa-solid fa-star"></i>
          <i :id="idPath" data-id="4" class="fa-solid fa-star"></i>
          <i :id="idPath" data-id="5" class="fa-solid fa-star"></i>
        </div> -->
      </ul>
    </div>
  </div>
 </div>
</template>

<script>
import ModalView from "@/components/ModalView.vue"
import MovieDetail from "@/components/MovieDetail.vue"
import notFoundImg from '@/assets/not-found-image.jpeg'
import StarRating from 'vue-star-rating'

export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  },
  components: {
    ModalView,
    MovieDetail,
    StarRating,
  },
  data: function () {
    return {
      isModalViewed: false,
    }
  },
  methods: {
    showModal () {
      document.body.classList.add("modal-open");
    },
  },
  computed: {
    posterPath: function () {
      const poster_path = this.movie.poster_path
      if (poster_path) {
        return `https://image.tmdb.org/t/p/original/${poster_path}`
      } else {
        return notFoundImg
      }
    },
    idPath: function () {
      return `movie-${ this.movie.id || this.movie.tmdb_movie_id }`
    }
  },
//   mounted() {
//     const voteAverage = Math.round(this.movie.vote_average / 2)
//     const stars = document.querySelectorAll(`#movie-${ this.movie.id || this.movie.tmdb_movie_id }`)
//     for(let star of stars) {
//       const num = star.dataset.id
//       if(voteAverage - num >= 0) {
//         if (!star.classList.contains('star-active')) {
//           star.classList.add('star-active')
//         }
//       } 
//     }
//   },
//   updated() {
//     const voteAverage = Math.round(this.movie.vote_average / 2)
//     const stars = document.querySelectorAll(`#movie-${ this.movie.id || this.movie.tmdb_movie_id }`)
//     for(let star of stars) {
//       const num = star.dataset.id
//       if(voteAverage - num >= 0) {
//         if (!star.classList.contains('star-active')) {
//           star.classList.add('star-active')
//         }
//       } else {
//         if (star.classList.contains('star-active')) {
//           star.classList.remove('star-active')
//         }
//       }
//     }
//   }
}

</script>

<style>
.flip-card {
  width: 15rem;
  height: 20rem;
  position: relative;
  transform-style: preserve-3d;
  transition: .3s .1s;
  margin-left : 2rem;
  cursor: pointer;
}

.flip-card:hover,
.flip-card:focus {
  transform: rotateY(180deg);
}

.card-front,
.card-back {
  width: 100%;
  height: 100%;
  border-radius: 24px;

  background: var(--dark);
  position: absolute;
  top: 0;
  left: 0;
  overflow: hidden;

  backface-visibility: hidden;

  display: flex;
  justify-content: center;
  align-items: center;
}

/* .card-front */
.card-front {
  transform: rotateY(0deg);
  z-index: 2;
}

/* .card-back */
.card-back {
  transform: rotateY(180deg);
  z-index: 1;
}

/* figure */
figure {
  z-index: -1;
}

/* figure, .img-bg */
figure,
.img-bg {
  position: absolute;
  top: 0;
  left: 0;

  width: 100%;
  height: 100%;
}

/* img */
.flip-card img {
  width: 100%;
  height: 100%;
  border-radius: 24px;
}


/* .img-bg */

.card-back .img-bg {
  background: rgba(0, 0, 0, 0.493);
}

.card-ul {
  list-style: none;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin-right: 2rem;
}


.card-ul li {
  width: 100%;
  margin-top: 12px;
  padding-bottom: 12px;
  font-size: 1.5rem;
  text-shadow: rgba(255, 255, 255, 0.308) 1px 1px;
  text-align: center;
  position: relative;
}

.fa-star {
  font-size: 1.2rem;
  color: rgb(0, 0, 0);
  animation: neon1 1.5s ease-in-out infinite alternate;
  transition: .3s;
}

.star-active {
  transform: scale(1.1);
  color: #ffffffe8;
}

@keyframes neon1 {
  from {
    text-shadow: 0 0 1px rgba(255, 255, 255, 0.575), 0 0 2px rgba(255, 255, 255, 0.671), 0 0 3px rgba(255, 255, 255, 0.726), 0 0 4px #00adb9,
      0 0 5px #0066aa, 0 0 6px #bd0153, 0 0 7px #4c00c7, 0 0 8px #00adb9;
  }
  to {
    text-shadow: 0 0 2px rgba(255, 255, 255, 0.747), 0 0 4px rgba(255, 255, 255, 0.651), 0 0 6px rgba(255, 255, 255, 0.644), 0 0 8px #00adb9,
      0 0 10px #0066aa, 0 0 12px #bd0153, 0 0 14px #4c00c7, 0 0 16px #00adb9;
  }
}
</style>