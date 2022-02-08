<template>
  <slidebar></slidebar>
  <menubar></menubar>
</template>

<script>
  import menubar from '../../components/MenuBar.vue'
  import slidebar from './base/Slidebar.vue'
  export default {
    components: {
      menubar,
      slidebar
    }
  }
</script>

<style>
</style>
