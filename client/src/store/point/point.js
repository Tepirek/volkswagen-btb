import API from '@/store/api/point/point'

const defaultPoint = {
  x: 0,
  y: 0,
  errorType: null,
  inclusionType: null
}

const state = {
  loading: false,
  points: [],
  point: { ...defaultPoint }
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
  },
  create ({ commit }, data) {
    return API.create(data)
      .then(response => {
        commit('appendPoint', response)
      })
  },
  delete ({ commit, dispatch }, id) {
    return API.delete(id)
      .then(response => {
        dispatch('notification/snackbar/success', {
          text: 'notifications.delete_point'
        }, { root: true })
      })
  },
  updatePoint ({ commit }, point) {
    commit('setPoint', { ...point })
  },
  removePoint ({ commit, state }, id) {
    const index = state.points.findIndex(e => e.id === id)
    if (index > -1) {
      state.points.splice(index, 1)
      commit('setPoints', [...state.points])
    }
  }
}

const mutations = {
  setLoading (state, value) {
    state.loading = value
  },
  setPoints (state, points) {
    state.points = points
  },
  setPoint (state, point) {
    state.point = point
  },
  appendPoint (state, point) {
    state.points.push(point)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
