import axios from 'axios'

export default class {
  static getBaseUrl () {
    return '/api/v1/summary/'
  }

  static fetchAll (data) {
    return new Promise((resolve, reject) => {
      axios.get(this.getBaseUrl(), {
        params: data
      })
        .then(response => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error.data)
        })
    })
  }

  static fetch (id) {
    return new Promise((resolve, reject) => {
      axios.get(`${this.getBaseUrl()}${id}/`)
        .then(response => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error.data)
        })
    })
  }

  static create (data) {
    return new Promise((resolve, reject) => {
      axios.post(this.getBaseUrl(), data)
        .then(response => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error.data)
        })
    })
  }
}
