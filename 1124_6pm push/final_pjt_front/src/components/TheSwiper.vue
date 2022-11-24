<template>
  <div class="swiper-box">
    <swiper class="swiper" :options="swiperOption">
      <swiper-slide v-for="(movie, idx) in movies" :key="idx" :movie="movie">
        <MovieCard2 :movie="movie" />
      </swiper-slide>
      <!-- <swiper-slide>
        <MovieCard v-for="(movie, idx) in movies" :key="idx" :movie="movie"/>
      </swiper-slide>
      <swiper-slide>
        <MovieCard v-for="(movie, idx) in movies" :key="idx" :movie="movie"/>
      </swiper-slide>
      <swiper-slide>
        <MovieCard v-for="(movie, idx) in movies" :key="idx" :movie="movie"/>
      </swiper-slide> -->
      <br><br><br><br>
      <div class="swiper-pagination" slot="pagination"></div>
      <div class="swiper-button-prev" slot="button-prev"></div>
      <div class="swiper-button-next" slot="button-next"></div>
    </swiper>
  </div>
</template>

<script>
import 'swiper/dist/css/swiper.css'
// import MovieList from '@/components/MovieList.vue'
import { swiper, swiperSlide } from 'vue-awesome-swiper'
// import { swiper, } from 'vue-awesome-swiper'
import MovieCard2 from '@/components/MovieCard.vue'


export default {
  name:'TheSwiper',
  components: {
    swiper,
    swiperSlide,
    MovieCard2,
    // MovieList,
  },
  props :{
    movies : {
      type: Array,
    },
  },
  data() {
    return {
      swiperOption: {
        effect: 'coverflow',
        grabCursor: true,
        centeredSlides: true,
        slidesPerView: '5',
        loop: true,
          coverflowEffect: {
          rotate: 30,
          stretch: 0,
          depth: 200,
          modifier: 0.5,
          slideShadows : true,
        },
        spaceBetween: 30,
        pagination: {
          el: '.swiper-pagination',
          clickable: true
        },
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev'
        },
        autoplay: {
          delay: 2500,
          disableOnInteraction: true,
        },
      }
    }
  },
  
  // mounted() {
	// 		//console.log('Current Swiper instance object', this.swiper)
	// 	this.swiper.slideTo(2, 1000, false)
  // }
}
</script>

<style>
.swiper-box {

  z-index: 1;
}
.swiper {
  height: 300px;
  width: 80%;
}

swiper-slide {
  display:flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  font-weight: bold;
}
</style>