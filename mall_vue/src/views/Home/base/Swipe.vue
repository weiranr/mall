<template>
  <div class="swipe-wrapper">
    <van-swipe :autoplay="3000">
      <van-swipe-item v-for="(image, index) in bannerImages" :key="index">
        <img v-lazy="image.carousel_url" />
      </van-swipe-item>
    </van-swipe>
  </div>
</template>

<script>
  import { mapState, mapMutations } from 'vuex'
  export default {
    methods: {
      ...mapMutations(['SET_BANNER_IMAGES']),
      getBannerImage() {
        this.$api.homeData.banner().then((
          data
        ) => {
          this.SET_BANNER_IMAGES(data)
        })
      }
    },
    computed: {
      ...mapState(['bannerImages'])
    },
    mounted() {
      this.getBannerImage()
    }
  }
</script>

<style>
  .swipe-wrapper img {
    max-width: 100%;
    /* height: auto; */
  }
  .van-swipe-item {
    text-align: center;
  }
</style>
