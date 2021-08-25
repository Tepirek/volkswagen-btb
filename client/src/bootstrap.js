import Vue from 'vue'
import Vuetify from 'vuetify'
import Vuex from 'vuex'
import axios from 'axios'
import store from '@/store'

import vuexI18n from 'vuex-i18n'
import pl from '@/i18n/pl'
import us from '@/i18n/us'
import ua from '@/i18n/ua'

import { BASE_URL } from './constants'

import LS from '@/services/localStorage'

window.Vue = Vue
window.Vuetify = Vuetify
window.Vuex = Vuex

window.LS = LS

if (!LS.get('settings')) {
  LS.set('settings', JSON.stringify({
    lang: 'pl'
  }))
}
const settings = JSON.parse(LS.get('settings'))

Vue.use(vuexI18n.plugin, store)
Vue.i18n.add('pl', pl)
Vue.i18n.add('us', us)
Vue.i18n.add('ua', ua)
Vue.i18n.set(settings.lang)

axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'
axios.defaults.headers.common['Content-Type'] = 'application/json'
axios.defaults.baseURL = BASE_URL
axios.defaults.timeout = 20000

axios.interceptors.request.use(config => {
  const AUTH_TOKEN = LS.get('auth.token.access')
  if (AUTH_TOKEN) {
    config.headers.common.Authorization = `Bearer ${AUTH_TOKEN}`
  }
  return config
}, error => {
  return Promise.reject(error)
})

axios.interceptors.response.use(response => {
  return response
}, async error => {
  const config = error.config
  if (config.url !== '/api/token/refresh/' && error.response) {
    if (error.response.status === 403 && !config._retry) {
      config._retry = true
      try {
        await store.dispatch('auth/refresh')
        config.headers.Authorization = `Bearer ${LS.get('auth.token.access')}`
        return axios(config)
      } catch (err) {
        store.dispatch('auth/logout')
      }
    }
  } else if (config.url === '/api/token/refresh/' && error.response && error.response.status === 401) {
    store.dispatch('auth/logout')
  }
  return error
})
