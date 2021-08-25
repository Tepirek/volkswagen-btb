import API from '@/store/api/componentType/componentType'
import { BASE_URL } from '@/constants'

const state = {
  isInit: false,
  loading: false,
  componentTypes: null,
  componentType: {
    name: '',
    image: ''
  }
}

const getters = {}

const actions = {
  fetchAll ({ commit, state, dispatch }, data) {
    commit('setLoading', true)
    return API.fetchAll(data)
      .then(response => {
        commit('setComponentTypes', { ...convertArrayToObject(response) })
        dispatch('updateComponentType', 0)
        commit('setLoading', false)
        commit('setInit', true)
      })
  },
  updateComponentType ({ commit, state }, number) {
    const l = Object.keys(state.componentTypes).length
    const index = state.componentType ? Object.keys(state.componentTypes).indexOf(state.componentType.name) : 0
    var next = mod(index + number, l)
    const key = getNthKeyName(state.componentTypes, next)
    commit('setComponentType', { ...state.componentTypes[key][0] })
  },
  toggleComponentType ({ commit, state }) {
    const name = state.componentType.name
    const currentSide = state.componentType.is_inner
    const index = state.componentTypes[name].findIndex(e => e.is_inner !== currentSide)
    commit('setComponentType', { ...state.componentTypes[name][index] })
  }
}

const mutations = {
  setLoading (state, value) {
    state.loading = value
  },
  setComponentTypes (state, componentTypes) {
    state.componentTypes = componentTypes
  },
  setComponentType (state, componentType) {
    state.componentType = componentType
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

const convertArrayToObject = (data) => {
  const componentTypes = {}
  data.forEach(entry => {
    entry.image = BASE_URL + entry.image
    if (entry.name in componentTypes) {
      componentTypes[`${entry.name}`].push(entry)
    } else {
      componentTypes[`${entry.name}`] = [entry]
    }
  })
  return componentTypes
}

const getNthKeyName = (data, number) => {
  return Object.keys(data)[number]
}

const mod = (n, m) => {
  return ((n % m) + m) % m
}
