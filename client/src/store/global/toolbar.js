const state = {
  text: ''
}

const getters = {}

const actions = {
  updateText ({ commit }, value) {
    commit('setText', value)
  }
}

const mutations = {
  setText (state, value) {
    state.text = value
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
