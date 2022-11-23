<template>
	<div>
		<b-button v-b-modal.modal.modal-1>더보기</b-button>
		
		<b-modal id="modal-1" title="Actors & Keywords" ok-only hide-header-close>
			<p>Actors :</p>
			<br>
			<p>Keywords :</p>
		</b-modal>
	</div>
</template>

<script>
export default {
	name: 'MovieDetailAdd',
}
</script>

<style>

</style>