<template>
  <transition name="modal">
    <div class="modal-container">
      <slot />
      <a @click="$emit('close-modal'), hideModal()" class="modal-close-button">
        x
        <!-- <i class="fa-solid fa-xmark close-mark"></i> -->
      </a>
    </div>
  </transition>
</template>

<script>
export default {
  methods: {
    hideModal () {
      document.body.classList.remove("modal-open");
    }
  }
}
</script>

<style>
.modal-container {
  position: fixed;
  z-index: 10;
  top: 5%;
  left: 5%;
  width: 90%;
  height: 90%;
  overflow-y: auto;
  background-color: rgba(0, 0, 0, 0.89);
  box-shadow: 0 15px 25px rgba(0,0,0,.6);
}

.modal-close-button {
  position: fixed;
  top: 0%;
  right: 0%;
  margin: 2%;
}

.close-mark {
  font-size: 30px;
  color: white;
}

::-webkit-scrollbar {
  display: none;
}
</style>