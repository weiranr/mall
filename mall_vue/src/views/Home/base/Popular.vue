<template>
  <van-row v-for="(goods,index) in data" :key="index" type="flex">
    <van-col span="12">
      <img :src="'http://127.0.0.1:8088/static/image'+goods[0].goods_cover_img" style="width: 100%;">
      {{ goods[0].goods_name }} <br>
      <span>￥</span><span style="font-size: 20px;">{{ goods[1].selling_price }}</span>
    </van-col>
    <van-col span="12">
      <img :src="'http://127.0.0.1:8088/static/image'+goods[1].goods_cover_img" style="width: 100%;" >
      {{ goods[1].goods_name }} <br>
      <span>￥</span><span style="font-size: 20px;">{{ goods[1].selling_price }}</span>
    </van-col>
  </van-row>
</template>

<script>
  export default {
    data() {
      return {
        data: [],
        temp: []
      }
    },
    methods: {
      getIndexConfig() {
        this.$api.homeData.indexconfig().then((
          data
        ) => {
          for (let i = 0; i < data.length; i++) {
            this.$api.homeData.findGoodsById(data[i].goods_id).then((data) => {
              if (this.temp.length === 2) {
                this.data.push(this.temp)
                this.temp = []
              } else {
                this.temp.push(data.data[0])
              }
            })
          }
        })
      }

    },
    mounted() {
      this.getIndexConfig()
    }
  }
</script>

<style>
  span {
    color: #ff4142;
  }
</style>
