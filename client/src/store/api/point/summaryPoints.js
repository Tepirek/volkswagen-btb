import axios from 'axios'

export default class {
  static getBaseUrl () {
    return '/api/v1/points/summary/'
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
}
