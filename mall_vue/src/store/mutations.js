export default {
  SET_BANNER_IMAGES(state, images) {
    state.bannerImages = images
    localStorage.setItem('bannerImages', JSON.stringify(images))
  },
  set_search_list(state, searchList) {
    state.searchList = searchList
  },
  set_category_level(state, data) {
    state.category_level.push(data)
  },
  set_goods_list(state, goodslist) {
    state.goodsList = goodslist
  }
}
