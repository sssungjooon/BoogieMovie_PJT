<template>
  <div class="review-page">
    <br><br>
    <h1>Review Page</h1>
    <router-link :to="{ name: 'CreateView' }">[CREATE]</router-link>
    <hr>
    <ReviewList/>
  </div>
</template>

<script>
import ReviewList from '@/components/ReviewList'


export default {
  name: 'ReviewView',
  components: {
    ReviewList,
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getReview()
  },
  methods: {
    getReview() {
      if (this.isLogin === true) { 
        this.$store.dispatch('getReview')
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LogInView'})
      }
    }
  }
}
</script>

<style>
.review-page {
  width : 100vw;
  height: 100vh;
  border: 10px;
  display: static;
  z-index: 1;
  justify-content: space-between;
}
</style>
