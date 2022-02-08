import { createStore } from 'vuex'
import state from './state.js'
import mutations from './mutations.js'
import actions from './actions.js'
import getters from './getters.js'
import modules from './modules.js'

export default createStore({
  state,
  mutations,
  actions,
  getters,
  modules
})
