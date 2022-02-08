<template>
  <swipe></swipe>
  <grid></grid>
  <popular></popular>
  <menubar></menubar>
</template>

<script>
  import menubar from '../../components/MenuBar.vue'
  import swipe from './base/Swipe.vue'
  import grid from './base/Grid.vue'
  import popular from './base/Popular.vue'
  export default {
    components: {
      menubar,
      swipe,
      grid,
      popular
    }
  }
</script>

<style>
</style>
