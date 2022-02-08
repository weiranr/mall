import axios from '../http.js'

const categoryData = {
  async goodscategory() {
    return await axios.get('goodscategory/')
  },
  async goodsinfo() {
    return await axios.get('goodsinfo/')
  }

}
export default categoryData
