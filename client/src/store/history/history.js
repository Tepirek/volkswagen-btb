import API from '@/store/api/logger/logger'

const state = {
  isInit: false,
  loading: {
    many: false
  },
  logs: null
}

const getters = {}

const actions = {
  fetchAll ({ commit }) {
    commit('setLoadingMany', true)
    return API.fetchAll()
      .then(response => {
        commit('setLogs', response)
        commit('setLoadingMany', false)
        commit('setInit', true)
      })
  }
}

const mutations = {
  setInit (state, value) {
    state.isInit = value
  },
  setLoadingMany (state, value) {
    state.loading = { ...state.loading, many: value }
  },
  setLogs (state, logs) {
    state.logs = logs
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
