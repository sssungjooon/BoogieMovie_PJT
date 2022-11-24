<template>
  <div>
    <h5>{{ review.id }}</h5>
    <p>작성자 : {{ review.username }}</p>
    <p>{{ review.title }}</p>
    <router-link :to="{ name: 'DetailReview', params: { id: review.id } }">
      [DETAIL]
    </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ReviewListItem',
  props: {
    review: Object,
  }
}
</script>

<style>

</style>
