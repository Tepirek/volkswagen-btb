const state = {
  queue: [],
  data: null,
  visible: false
}

const getters = {}

const actions = {
  success ({ dispatch }, entry) {
    dispatch('push', {
      color: 'success darken-1',
      icon: 'mdi-check-circle-outline',
      text: entry.text
    })
  },
  info ({ dispatch }, entry) {
    dispatch('push', {
      color: 'primary darken-1',
      icon: 'mdi-information-outline',
      text: entry.text
    })
  },
  error ({ dispatch }, entry) {
    dispatch('push', {
      color: 'error darken-1',
      icon: 'mdi-alert-circle-outline',
      text: entry.text
    })
  },
  push ({ commit, state, dispatch }, entry) {
    commit('addToQueue', { ...entry })
    if (!state.visible) {
      dispatch('pop')
    }
  },
  pop ({ commit, state }) {
    if (!state.visible && state.queue.length) {
      const item = state.queue[0]
      commit('setData', { ...item })
      commit('removeFromQueue')
      commit('setVisible', true)
    } else {
      commit('setVisible', false)
    }
  },
  updateVisible ({ commit }, value) {
    commit('setVisible', value)
  }
}

const mutations = {
  addToQueue (state, entry) {
    state.queue.push(entry)
  },
  removeFromQueue (state) {
    state.queue.splice(0, 1)
  },
  setData (state, data) {
    state.data = data
  },
  setVisible (state, value) {
    state.visible = value
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
