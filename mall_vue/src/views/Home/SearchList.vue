<template>
<ul v-for="(good, index) in searchList" :key="index">
  <li>{{ good.goods_id }}, {{ good.goods_name }}, {{ good.goods_intro }} ￥{{ good.selling_price }} <br><br><br></li>
</ul>
</template>

<script>
  import { mapState } from 'vuex'
  export default {
    computed: {
      ...mapState(['searchList'])
    }
  }
</script>

<style>
</style>
