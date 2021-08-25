import API from '@/store/api/report/report'

const state = {
  isInit: false,
  loading: {
    one: false,
    many: false
  },
  reports: [],
  report: {}
}

const getters = {}

const actions = {
  fetchAll ({ commit }) {
    commit('setLoadingMany', true)
    commit('setReports', [])
    return API.fetchAll()
      .then(response => {
        commit('setReports', response)
        commit('setLoadingMany', false)
      })
  },
  fetchOne ({ commit }, slug) {
    commit('setLoadingOne', true)
    return API.fetchOne(slug)
      .then(response => {
        commit('setReport', response)
        commit('setLoadingOne', false)
        commit('setInit', true)
      })
  },
  create ({ commit, dispatch }, data) {
    commit('setLoadingOne', true)
    return API.create(data)
      .then(response => {
        commit('setReport', response)
        commit('setInit', true)
        dispatch('notification/snackbar/success', {
          text: 'notifications.create_report'
        }, { root: true })
        commit('setLoadingOne', false)
      })
  },
  update ({ commit, dispatch }, id) {
    return API.update(id)
      .then(_ => {
        commit('setReport', {})
        dispatch('notification/snackbar/success', {
          text: 'notifications.update_report'
        }, { root: true })
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
  setReports (state, reports) {
    state.reports = reports
  },
  setReport (state, report) {
    state.report = report
  },
  setInit (state, value) {
    state.isInit = value
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
