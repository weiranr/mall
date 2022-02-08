<template>
  <van-search v-model="value" show-action background='pink' @search="onSearch" placeholder="请输入搜索关键词">
    <template #action>
        <div @click="onSearch(value)">搜索</div>
      </template>
    <template #left >
      <div @click.prevent="back($event)"><van-icon name="arrow-left" :style="{display: isdisplay}"/></div>
    </template>
  </van-search>
</template>

<script>
  import { mapMutations } from 'vuex'
  export default {
    data() {
      return {
        value: '',
        isdisplay: 'none'
      }
    },
    methods: {
      ...mapMutations(['set_search_list']),
      onSearch(val) {
        this.isdisplay = 'inline'
        this.$api.homeData.search(val).then((
          data
        ) => {
          this.set_search_list(data.data)
          this.$router.push('/Home/SearchList')
        })
      },
      back(e) {
        this.isdisplay = 'none'
        this.$router.go(-1)
      }
    }
  }
</script>

<style>
</style>
