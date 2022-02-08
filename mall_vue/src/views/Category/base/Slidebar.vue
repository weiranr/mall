<template>
  <van-row>
    <van-col span="5">
      <van-sidebar v-for="(level1, index) in category_level[0]" :key="index" @click='select($event)'>
        <van-sidebar-item replace :to="'/Category/level2r'+(index+1)" :title="level1.category_name"/>
      </van-sidebar>
    </van-col>
    <van-col span="19"><router-view></router-view></van-col>
  </van-row>

</template>

<script>
  import { mapState, mapMutations } from 'vuex'
  export default {
    data() {
      return {
      }
    },
    methods: {
      ...mapMutations(['set_category_level', 'set_goods_list']),
      getGoodsCategory() {
        this.$api.categoryData.goodscategory().then((data) => {
          var l1 = []
          var l2 = []
          var l3 = []
          for (var i = 0; i < data.length; i++) {
            if (data[i].category_level === '1') {
              l1.push(data[i])
            } else if (data[i].category_level === '2') {
              l2.push(data[i])
            } else if (data[i].category_level === '3') {
              l3.push(data[i])
            }
          }
          this.set_category_level(l1)
          this.set_category_level(l2)
          this.set_category_level(l3)
        })
        this.$api.categoryData.goodsinfo().then((data) => {
          this.set_goods_list(data)
        })
      },
      select(e) {
        var parent = e.target.parentElement.parentElement.parentElement
        for (var i = 0; i < parent.children.length; i++) {
          var n = parent.children[i].querySelector('div')
          // n.setAttribute('class', 'van-sidebar-item')
          n.style.backgroundColor = 'white'
        }
        // e.target.parentNode.setAttribute('class', 'van-sidebar-item van-sidebar-item--select')
      e.target.parentNode.style.backgroundColor = 'ghostwhite'
      }
    },
    computed: {
      ...mapState(['category_level', 'goodsList'])
    },
    mounted() {
      this.getGoodsCategory()
    }
  }
</script>

<style>
</style>
