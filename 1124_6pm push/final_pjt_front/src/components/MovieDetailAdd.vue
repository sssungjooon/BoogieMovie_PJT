<template>
	<div class="second-info-section">
		<div class="detail-genre">
			<h4>장르 : </h4>
			<br>
			<div>
				<p v-for="genre in movieGenre" :key="genre">{{ genre_name }} </p>
			</div>
		</div>
			<!-- <a v-for="(genre, idx) in movieGenre" :key="idx" :genre="genre">{{ genre_name }}</a> -->
		<div class="more-info">
			<h4 class="actor_info">배우 정보</h4>
			<section class="information-container">
				<!-- <MovieCard v-for="(movie, idx) in movies" :key="idx" :movie="movie" /> -->
				<ActorListItem v-for="(actor, idx) in movieActor" :key="idx" :actor="actor" class="actors"/>
			</section>
		</div>

		<div class="add-button">
			<a href="http://localhost:8080/review">
				<button>Review</button>
			</a>
			<!-- <b-button v-b-modal.modal.modal-1>더보기</b-button>
			
			<b-modal id="modal-1" title="Actors & Keywords" ok-only hide-header-close>
				<p>Actors :</p>
				<br>
				<p>Keywords :</p>
			</b-modal> -->
		</div>
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
	font-size: 25px;
	text-align: left;
}

.add-button {
	position: fixed;
	top:60%;
	right:17%;
	
}

/* .information-container {
	position: fixed;
	top:20%;
	right:7%;
	width: 30%;
} */

/* s */

.second-info-section {
	margin-top: 30px;
}
.detail-genre {
	text-align: left;
}


.more-info {
	width: auto;
}
</style>