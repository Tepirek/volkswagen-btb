import axios from 'axios'

export default class {
  static getBaseUrl () {
    return '/api/v1/logs/'
  }

  static fetchAll () {
    return new Promise((resolve, reject) => {
      axios.get(this.getBaseUrl())
        .then(response => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error.data)
        })
    })
  }
}
