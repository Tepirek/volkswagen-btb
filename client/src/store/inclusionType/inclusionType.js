import API from '@/store/api/inclusionType/inclusionType'
import { BASE_URL } from '../../constants'

const state = {
  loading: false,
  inclusionTypes: [],
  inclusionType: null
}

const getters = {}

const actions = {
  fetchAll ({ commit }) {
    commit('setLoading', true)
    return API.fetchAll()
      .then(response => {
        commit('setInclusionTypes', [...preprocessData(response)])
        commit('setLoading', false)
      })
  },
  updateInclusionType ({ commit }, inclusionType) {
    commit('setInclusionType', inclusionType)
  }
}

const mutations = {
  setLoading (state, value) {
    state.loading = value
  },
  setInclusionTypes (state, inclusionTypes) {
    state.inclusionTypes = inclusionTypes
  },
  setInclusionType (state, inclusionType) {
    state.inclusionType = inclusionType
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
