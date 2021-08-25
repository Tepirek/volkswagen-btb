import API from '@/store/api/color/color'

const state = {
  loading: false,
  colors: []
}

const getters = {}

const actions = {
  fetchAll ({ commit }) {
    commit('setLoading', true)
    return API.fetchAll()
      .then(response => {
        commit('setColors', response)
        commit('setLoading', false)
      })
  }
}

const mutations = {
  setLoading (state, value) {
    state.loading = value
  },
  setColors (state, colors) {
    state.colors = colors
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
