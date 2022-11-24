<template>
  <div class="actor-box">
    <div class="photo-container">
      <img :src="actor_profile" class="actor_pic" />
    </div>
    <h6>{{ actor_name }}</h6>
  </div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'ActorListItem',
	components : {

	},
	props : {
		actor : Number,
	},
  data: function() {
    return {
      //selectedMovies: [],
      actor_id : '',
      actor_name : '',
      actor_profile : '',
    }
  },
  methods : {
    getActorsInfo : function(){
      const actor_id = this.actor
      const link5 = `http://127.0.0.1:8000/movies/actors/${actor_id}`
      axios.get(link5)
        .then(res =>{
          this.actor_id = res.data.id
          this.actor_name = res.data.name
          this.actor_profile = res.data.profile_path
          //this.highscore_movies = res.data.highscore_movies
          //this.like_movies = res.data.like_movies
        })
    }
  },
  created : function(){
    this.getActorsInfo()
  },
}
</script>

<style>
/* .photo-container {
  height: 30px;
  width: 30px;
} */

.actor_pic {
  height: 120px;
  width: 80px;  
}

</style>