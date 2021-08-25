import axios from 'axios'

export default class {
  static getBaseUrl () {
    return 'auth/user/'
  }

  static getAuthTokenUrl () {
    return '/api/token/'
  }

  static getAuthTokenRefreshUrl () {
    return '/api/token/refresh/'
  }

  static fetch () {
    return new Promise((resolve, reject) => {
      axios.get(`${this.getBaseUrl()}`)
        .then(response => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error.data)
        })
    })
  }

  static login (data) {
    return new Promise((resolve, reject) => {
      axios.post(this.getAuthTokenUrl(), data)
        .then(response => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error.data)
        })
    })
  }

  static refresh (data) {
    return new Promise((resolve, reject) => {
      axios.post(this.getAuthTokenRefreshUrl(), data)
        .then(response => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error.data)
        })
    })
  }
}
