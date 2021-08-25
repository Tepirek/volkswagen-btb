export default {
  get (key) {
    return localStorage.getItem(key) || null
  },
  set (key, value) {
    return localStorage.setItem(key, value)
  },
  remove (key) {
    return localStorage.removeItem(key)
  }
}
