<template>
  <div class="my-page">
    <br><br><br>
    <p style="font-size:30px">MyPage</p><br>
    <div id="mypage">
      <span class="mypage-router">
        <router-link class="router" style="text-decoration:none; color: white;" :to="{name:'likedmovies'}">Liked Movies</router-link> |
        <router-link class="router" style="text-decoration:none; color: white;" :to="{name:'userreviews'}">My Reviews</router-link> |
        <router-link class="router" style="text-decoration:none; color: white;" :to="{name:'changeinfo'}">Change Info</router-link>
     
      </span>
    </div>
    <router-view/>
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
.my-page {
  width : 100vw;
  height: 100vh;
  border: 10px;
  display: static;
  z-index: 1;
  justify-content: space-between;
}
#mypage {
  z-index: 2;
}
.mypage-router {
  font-size: 20px;
}
.router:hover {
  background-color: rgb(75, 4, 20);
  transition: all .5s;
  transform: translateY(-0.25em);
  color: black;
}
</style>
