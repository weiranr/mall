<template>
  <search></search>
  <router-view></router-view>
</template>

<script>
  import search from './base/Search.vue'
  export default {
    components: {
      search
    }
  }
</script>

<style>
</style>
