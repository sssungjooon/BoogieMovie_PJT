<template>
  <div class="movie-review-section">
    <p class="review-text">Reviews</p>
    <div id="review-input-box">
      <div class="star-rate-box">
        <i :id="reviewIdPath" data-id="1" class="fa-solid fa-star" @click="selectStar"></i>
        <i :id="reviewIdPath" data-id="2" class="fa-solid fa-star" @click="selectStar"></i>
        <i :id="reviewIdPath" data-id="3" class="fa-solid fa-star" @click="selectStar"></i>
        <i :id="reviewIdPath" data-id="4" class="fa-solid fa-star" @click="selectStar"></i>
        <i :id="reviewIdPath" data-id="5" class="fa-solid fa-star" @click="selectStar"></i>
      </div>
      <div v-if="reviewed">
        <div class="myreview-content">
          <p>{{ myreview.content }}</p>
        </div>
        <div class="submit-buttons">
          <button @mousedown="editReview()" class="btn btn-link">Update</button>
          <button @click="deleteReview()" class="btn btn-link">Delete</button>
        </div>
      </div> 
    </div>
    <div v-if="!reviewed" class="review-content-input-box">
      <textarea @keypress.enter="submitReview()" v-model="myreview.content" type="text" name="" class="review-content-input" placeholder="Write the review..." required />
      <div class="input-submit-buttons">
        <button @mouseenter="onVoice" class="btn btn-link input-voice-btn">
          <i class="fa-solid fa-microphone"></i>
        </button>
        <button @click="submitReview()" class="btn btn-link input-submit-bnt">Submit</button>
      </div>
    </div>
    <div style="margin-top: 2rem;">
      <ReviewList v-if="othersreviewed" :reviews="reviews" />
      <div v-else class="none-review-text">There are no reviews written yet...</div>
    </div>
  </div>
</template>

<script>
import ReviewList from '@/components/ReviewList.vue'
// import axios from 'axios'
// import drf from '@/api/drf'
import { mapGetters } from 'vuex'

export default {
  name: "MovieDetailReview",
  components: {
    ReviewList,
  },
  props: {
    movieId: Number,
  },
  data: function () {
    return {
      reviewed: false,
      othersreviewed: false,
      reviews: [],
      myreview: {
        'content': '',
        'score': 0,
      },
    }
  },
  // methods: {
  //   onVoice: function () {
  //     window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
  //     const recognition = new window.SpeechRecognition();
  //     recognition.interimResults = false;
  //     recognition.lang = 'ko-KR'; 

  //     let p = ''
    
  //     recognition.addEventListener('result', e => {
  //     const transcript = Array.from(e.results)
  //       .map(result => result[0])
  //       .map(result => result.transcript)
  //       .join('');

  //       p = transcript;
  //       this.myreview.content += p

  //       if (e.results[0].isFinal) {
  //         p = ' '
  //         this.myreview.content += p
  //       }
  //     });    

  //     recognition.start();
  //   },
  //   deleteReview () {
  //     axios({
  //       url: drf.movies.review_ud(this.movieId, this.myreview.id),
  //       method: 'delete',
  //       headers: this.authHeader
  //     })
  //     this.reviewed = false
  //     this.myreview = {
  //       'content': '',
  //       'score': 0,         
  //     }
  //     this.updateStar()
  //   },
  //   editReview () {
  //     this.reviewed = false
  //   },
  //   updateStar () {
  //     const stars = document.querySelectorAll(`#movie-${ this.movieId }-review`)
  //     for (let star of stars) {        
  //       if (star.dataset.id <= this.myreview.score) {
  //         if (!star.classList.contains('star-active')) {
  //           star.classList.add('star-active')
  //         }
  //       } else {
  //          if (star.classList.contains('star-active')) {
  //           star.classList.remove('star-active')
  //         }
  //       }
  //     }
  //   },
  //   submitReview () {
  //     if ( this.myreview.score === 0 ) {
  //       alert('별점을 입력해주세요!')
  //       return
  //     }
  //     if (this.myreview.content === '') {
  //       alert('내용을 입력해주세요!')
  //       return
  //     }
  //     axios({
  //       url: drf.movies.reviews(this.movieId),
  //       method: 'post',
  //       headers: this.authHeader,
  //       data: {
  //         content: this.myreview.content,
  //         score: this.myreview.score,
  //       }
  //     })
  //     .then(res => {
  //       this.myreview = res.data
  //       this.reviewed = true
  //     })
  //   },
  //   selectStar: function (event) {
  //     if (!this.reviewed) {
  //       const selectScore = event.target.dataset.id
  //       this.myreview.score = selectScore
  //       const stars = document.querySelectorAll(`#movie-${ this.movieId }-review`)
  //       for (let star of stars) {
  //         if (star.dataset.id <= selectScore) {
  //           if (!star.classList.contains('star-active')) {
  //             star.classList.add('star-active')
  //           }
  //         } else {
  //            if (star.classList.contains('star-active')) {
  //             star.classList.remove('star-active')
  //           }
  //         }
  //       }
  //     }
  //   },
  // },
  computed: {
    ...mapGetters(['authHeader']),
    reviewIdPath: function () {
      return `movie-${ this.movieId }-review`
    }
  },
  // created () {
  //   axios({
  //     url: drf.movies.movie(this.movieId),
  //     method: 'get',
  //   })
  //   .then(res => {
  //     this.reviews = res.data.reviews
  //     axios({
  //       url: drf.accounts.currentUserInfo(),
  //       method: 'get',
  //       headers: this.authHeader
  //     })
  //     .then(res => {
  //       const userId = res.data.pk
  //       this.reviews.map(review => {
  //         if (review.user.id === userId) {
  //           this.reviewed = true
  //           this.myreview = review
  //         }
  //       })
  //       if (this.reviewed) {
          
  //         const idx = this.reviews.indexOf(this.myreview)
  //         this.reviews.splice(idx, 1)
  //       }
  //       if (this.reviews.length > 0) {
  //         this.othersreviewed = true
  //       }
  //     })
  //   })
  // },
  // updated () {
  //   this.updateStar()
  // }
}
</script>

<style>
.movie-review-section {
  width: 100%;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.star-rate-box {
  display: flex;
  justify-content: flex-start;
  margin: 0.5rem;
}

.review-text {
  color: white;
  font-size: 1.5rem;
  font-weight: bold;
  margin-left: 10px;
}

#review-input-box {
  width: 100%;
}

.review-content-input-box {
  width: 100%;
  display: flex;
  flex-direction: column;
  margin-top: 0px;
}

.review-content-input {
  width: 100%;
  height: 8rem;
  border-radius: 20px;
  background-color: rgba(255, 255, 255, 0.397);
  outline: none;
  border: none;
  border-right: 0px;
  border-top: 0px;
  border-left: 0px;
  border-bottom:0px;
  padding: 20px;
  padding-top: 20px;
  color: white;
}

.review-content-input text {
  color: white;
}

.review-content-input:focus { 
  box-shadow: 3px 3px 7px #01a8b1a4;
}

.review-content-input-box .input-submit-bnt {
  background: none;
  color:#00595e;
  text-decoration: none;
  position: relative;
  align-self: flex-end;
  transition: .3s;
}

.review-content-input-box button:hover,
.review-content-input-box button:focus,
.submit-buttons button:hover,
.submit-buttons button:focus {
  color: #00cbd6;
  transform: scale(1.1);
}

.myreview-content {
  color: white;
  width: 100%;
  height: 8rem;
  border-radius: 20px;
  background-color: rgba(255, 255, 255, 0.397);
  padding: 20px;
  text-align: start;
}

.input-submit-buttons {
  display: flex;
  justify-content: flex-end;
  position: relative;
  bottom: 35px;
}

.submit-buttons {
  display: flex;
  justify-content: flex-end;
}

.input-submit-buttons button,
.submit-buttons button {
  background: none;
  color: #00595e;
  text-decoration: none;
  transition: .3s;
}

.none-review-text {
  color: white;
  margin-bottom: 3rem;
}

.fa-star:hover {
  transform: scale(1.2);
}
</style>