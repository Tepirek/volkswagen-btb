import API from '@/store/api/bodyType/bodyType'

const state = {
  loading: false,
  bodyTypes: []
}

const getters = {}

const actions = {
  fetchAll ({ commit }) {
    commit('setLoading', true)
    return API.fetchAll()
      .then(response => {
        commit('setBodyTypes', response)
        commit('setLoading', false)
      })
  }
}

const mutations = {
  setLoading (state, value) {
    state.loading = value
  },
  setBodyTypes (state, bodyTypes) {
    state.bodyTypes = bodyTypes
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
