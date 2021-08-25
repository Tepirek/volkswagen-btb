import LS from '@/services/localStorage'
import API from '@/store/api/auth/auth'
import router from '@/router'

const AUTH_TOKEN = 'auth.token.access'
const AUTH_TOKEN_REFRESH = 'auth.token.refresh'
const AUTH_SUCCESS = 'success'
const AUTH_ERROR = 'error'
const REDIRECT_AFTER_LOGIN = '/profile'

const state = {
  accessToken: LS.get(AUTH_TOKEN),
  refreshToken: LS.get(AUTH_TOKEN_REFRESH),
  status: '',
  validationSuccess: '',
  validationError: '',
  loading: true,
  fetching: false,
  user: null
}

const getters = {
  isAuthenticated (state) {
    return !!state.accessToken
  },
  isInit (state) {
    return !!state.user
  },
  isFetching (state) {
    return !!state.fetching
  }
}

const actions = {
  login ({ commit, dispatch }, data) {
    return API.login(data)
      .then(async response => {
        LS.set(AUTH_TOKEN, response.access)
        LS.set(AUTH_TOKEN_REFRESH, response.refresh)
        commit('setAccessToken', response.access)
        commit('setRefreshToken', response.refresh)
        commit('setStatus', AUTH_SUCCESS)
        await dispatch('fetch')
        router.push(REDIRECT_AFTER_LOGIN)
      })
      .catch(_ => {
        dispatch('notification/snackbar/error', {
          text: 'auth.notifications.login_failure'
        }, { root: true })
        dispatch('resetTokens')
        commit('setStatus', AUTH_ERROR)
      })
  },
  logout ({ dispatch }) {
    dispatch('resetTokens')
    dispatch('notification/snackbar/success', {
      text: 'auth.notifications.logout_success'
    }, { root: true })
    router.push('/login')
  },
  refresh ({ commit, dispatch }) {
    return API.refresh({
      refresh: LS.get(AUTH_TOKEN_REFRESH)
    })
      .then(response => {
        const token = response.access
        LS.set(AUTH_TOKEN, token)
        commit('setAccessToken', token)
        commit('setStatus', AUTH_SUCCESS)
      })
      .catch(_ => {
        dispatch('resetTokens')
        commit('setStatus', AUTH_ERROR)
      })
  },
  resetTokens ({ commit }) {
    LS.remove(AUTH_TOKEN)
    LS.remove(AUTH_TOKEN_REFRESH)
    commit('setAccessToken', null)
    commit('setRefreshToken', null)
  },
  fetch ({ commit, dispatch }) {
    commit('setFetching', true)
    return API.fetch()
      .then(response => {
        commit('setUser', response)
        commit('setFetching', false)
      })
      .catch(_ => {
        dispatch('auth/logout')
      })
  }
}

const mutations = {
  setAccessToken (state, value) {
    state.accessToken = value
  },
  setRefreshToken (state, value) {
    state.refreshToken = value
  },
  setStatus (state, value) {
    state.status = value
  },
  setLoading (state, value) {
    state.loading = value
  },
  setFetching (state, value) {
    state.fetching = value
  },
  setUser (state, value) {
    state.user = value
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
