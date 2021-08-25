import API from '@/store/api/summary/summary'
import { BASE_URL } from '@/constants'

const state = {
  loading: {
    one: false,
    many: false
  },
  summaries: null,
  summary: null,
  filtersVisible: true,
  filters: null
}

const getters = {}

const actions = {
  fetchAll ({ commit, state, dispatch }) {
    commit('setLoadingMany', true)
    dispatch('resetSummaries')
    return API.fetchAll(state.filters)
      .then(response => {
        commit('setSummaries', [...preprocessData(response)])
        commit('setLoadingMany', false)
        dispatch('notification/snackbar/success', {
          text: 'notifications.all_summaries'
        }, { root: true })
      })
  },
  fetchOne ({ commit }, id) {
    commit('setLoadingOne', true)
    return API.fetchOne(id)
      .then(response => {
        commit('setSummary', response)
        commit('setLoadingOne', false)
      })
  },
  create ({ commit, dispatch }, data) {
    commit('setLoadingOne', true)
    return API.create(data)
      .then(response => {
        commit('setSummary', response)
        dispatch('notification/snackbar/success', {
          text: 'notifications.create_summary'
        }, { root: true })
        commit('setLoadingOne', false)
      })
      .catch(_ => {
        // TODO: add snackbar notification
      })
  },
  resetSummaries ({ commit }) {
    commit('setSummaries', null)
  },
  updateFiltersVisible ({ commit }, value) {
    commit('setFiltersVisible', value)
  },
  updateFilters ({ commit }, filters) {
    commit('setFilters', { ...filters })
  }
}

const mutations = {
  setLoadingOne (state, value) {
    state.loading.one = value
  },
  setLoadingMany (state, value) {
    state.loading.many = value
  },
  setSummaries (state, summaries) {
    state.summaries = summaries
  },
  setSummary (state, summary) {
    state.summary = summary
  },
  setFiltersVisible (state, value) {
    state.filtersVisible = value
  },
  setFilters (state, filters) {
    state.filters = filters
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
    if (entry.file) {
      entry.file = BASE_URL + entry.file
    }
  })
  return data
}
