import API from '@/store/api/errorType/errorType'
import { BASE_URL } from '../../constants'

const state = {
  loading: false,
  errorTypes: [],
  errorType: null
}

const getters = {}

const actions = {
  fetchAll ({ commit }) {
    commit('setLoading', true)
    return API.fetchAll()
      .then(response => {
        commit('setErrorTypes', [...preprocessData(response)])
        commit('setLoading', false)
      })
  },
  updateErrorType ({ commit }, errorType) {
    commit('setErrorType', errorType)
  }
}

const mutations = {
  setLoading (state, value) {
    state.loading = value
  },
  setErrorTypes (state, errorTypes) {
    state.errorTypes = errorTypes
  },
  setErrorType (state, errorType) {
    state.errorType = errorType
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
  data.forEach(entry => {
    if (entry.marker) {
      entry.marker = BASE_URL + entry.marker
    }
  })
  return data
}
