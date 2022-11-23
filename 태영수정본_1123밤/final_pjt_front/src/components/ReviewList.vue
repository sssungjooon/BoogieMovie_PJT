<template>
  <div id="review-item-box">
    <ReviewItem v-for="(review, idx) in reviews" :key="idx" :review="review"  />
  </div>
</template>

<script>
import ReviewItem from "@/components/ReviewItem.vue"

export default {
  name: "ReviewList",
  components: {
    ReviewItem
  },
  props: {
    reviews: Array,
  },
  data: function () {
    return {
      reviewed: this.reviews.length > 0
    }
  }
}
</script>

<style>

</style>