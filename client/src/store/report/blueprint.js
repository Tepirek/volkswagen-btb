import API from '@/store/api/report/blueprint'
import { BASE_URL } from '@/constants'

const state = {
  loading: {
    one: false,
    many: false
  },
  blueprints: null
}

const getters = {}

const actions = {
  fetchOne ({ commit }, id) {
    commit('setLoadingMany', true)
    return API.fetchOne(id)
      .then(response => {
        commit('setBlueprints', preprocessData(response))
        commit('setLoadingMany', false)
      })
  }
}

const mutations = {
  setLoadingOne (state, value) {
    state.loading.one = value
  },
  setLoadingMany (state, value) {
    state.loading.many = value
  },
  setBlueprints (state, blueprints) {
    state.blueprints = blueprints
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}

const preprocessData = (data) => {
  Object.entries(data).forEach((value, index) => {
    data[value[0]] = BASE_URL + value[1]
  })
  return data
}
