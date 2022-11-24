<template>
	<div class="second-info-section">
		<div>
			<h4>장르 : </h4>
			<div>
				<p v-for="genre in movieGenre" :key="genre">{{ genre_name }} </p>
			</div>
		</div>
			<!-- <a v-for="(genre, idx) in movieGenre" :key="idx" :genre="genre">{{ genre_name }}</a> -->
		<section class="information-container">
			<h2 class="actor_info">배우 정보</h2>
			<!-- <MovieCard v-for="(movie, idx) in movies" :key="idx" :movie="movie" /> -->
			<ActorListItem v-for="(actor, idx) in movieActor" :key="idx" :actor="actor"/>
		</section>
		<b-button v-b-modal.modal.modal-1>더보기</b-button>
		
		<b-modal id="modal-1" title="Actors & Keywords" ok-only hide-header-close>
			<p>Actors :</p>
			<br>
			<p>Keywords :</p>
		</b-modal>
	</div>
</template>

<script>
import ActorListItem from "@/components/ActorListItem.vue"
import axios from 'axios'

export default {
	name: 'MovieDetailAdd',
	components : {
		ActorListItem,
	},
	data: function() {
    return {
			genre : '',
			genre_id : '',
      genre_name : '',
    }
	},
	props : {
		movieActor: Array,
		movieGenre: Array,
	},
	methods : {
    getGenreInfo : function(){
      const genre_id = this.genre
      const link6 = `http://127.0.0.1:8000/movies/genres/${genre_id}`
      axios.get(link6)
        .then(res =>{
					this.genre_id = res.data.id
          this.genre_name = res.data.name
        })
    }
  },
  created : function(){
    this.getGenreInfo()
  },
}
</script>

<style>
.actor_info {
	text-align: top;
}

.information-container {
	/* width: 100%; */
  /* padding: 1rem; */
  /* display: flex;
  flex-direction: column;
  /* align-items: flex-start; */
	/* margin: 10px auto;
	position :relative; */
}


/* .second-info-section {
  width: 100%;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
} */

</style>