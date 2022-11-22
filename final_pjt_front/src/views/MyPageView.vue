<template>
  <div id="my-page">
    
    <p>mypage</p>
    <UserReviewItem/>
  </div>
</template>

<script>
import UserReviewItem from '@/components/UserReviewItem'
export default {
  name: 'MyPageView',
  components: {
    UserReviewItem,
  }
}
</script>

<style>
#mypage {
  width : 80%;
  height: 100%;
  background-color:navy;
  border: 10px;

}
</style>
