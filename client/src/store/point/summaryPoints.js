import API from '@/store/api/point/summaryPoints'

const state = {
  loading: false,
  points: []
}

const getters = {}

const actions = {
  fetchAll ({ commit }, data) {
    commit('setLoading', true)
    return API.fetchAll(data)
      .then(response => {
        commit('setPoints', response)
        commit('setLoading', false)
      })
  }
}

const mutations = {
  setLoading (state, value) {
    state.loading = value
  },
  setPoints (state, points) {
    state.points = points
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
