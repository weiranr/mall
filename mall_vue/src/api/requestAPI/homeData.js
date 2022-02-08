import axios from '../http.js'

const homeData = {
  async banner() {
    return await axios.get('mallcarousel/')
  },
  async indexconfig() {
    return await axios.get('indexconfig/')
  },
  async findGoodsById(gid) {
    return await axios.get('findgoods/', { params: { id: gid } })
  },
  async search(searchText) {
    return await axios.get('search/', { params: { name: searchText } })
  }
}
export default homeData
