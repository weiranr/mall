<template>
  <ul v-for="(jiajv,index) in category_level[1]" :key="index">
    <li v-if="jiajv.parent_id == '61'">{{ jiajv }}</li>
  </ul>
</template>

<script>
  import { mapState } from 'vuex'
  export default {
    computed: {
      ...mapState(['category_level'])
    }
  }
</script>

<style>
</style>
