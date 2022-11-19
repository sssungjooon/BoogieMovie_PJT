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

</style>
