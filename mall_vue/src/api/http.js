import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8088/'

/*
 * 设置超时请求时间
 */

axios.defaults.timeout = 10000

axios.defaults.headers['Content-Type'] = 'application/x-www-from-urlencoded'

/*
 * 设置请求拦截器
 */

axios.interceptors.response.use(
  response => {
    // 返回响应主体中的信息,例如知道服务器返回CODE值来知道成功还是失败
    return response.data
  },
  error => {
    return Promise.reject(error)
  }
)

export default axios
