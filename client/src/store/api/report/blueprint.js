import axios from 'axios'

export default class {
  static getBaseUrl () {
    return '/api/v1/reports/blueprint/'
  }

  static fetchOne (id) {
    return new Promise((resolve, reject) => {
      axios.get(`${this.getBaseUrl()}${id}`)
        .then(response => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error.data)
        })
    })
  }
}
