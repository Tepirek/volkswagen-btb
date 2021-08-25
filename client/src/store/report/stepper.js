const state = {
  step: 1,
  errorDialogVisible: true
}

const getters = {}

const actions = {
  updateStep ({ commit }, value) {
    commit('setStep', value)
  },
  updateErrorDialogVisible ({ commit }, value) {
    commit('setErrorDialogVisible', value)
  }
}

const mutations = {
  setStep (state, value) {
    state.step = value
  },
  setErrorDialogVisible (state, value) {
    state.errorDialogVisible = value
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
