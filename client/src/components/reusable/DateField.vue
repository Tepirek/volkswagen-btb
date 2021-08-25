<template>
  <div>
  <v-text-field
    append-icon="mdi-calendar"
    :label="label"
    :value="formattedDate"
    @mousedown="display = true"
  >
  </v-text-field>
  <v-dialog
    v-model="display"
    max-width="300px"
  >
    <v-date-picker
      @input="pickDate"
      :value="value"
      color="primary"
      :min="min"
      :max="max"
    ></v-date-picker>
  </v-dialog>
  </div>
</template>
<script>
export default {
  name: 'DateField',
  props: {
    label: String,
    value: String,
    min: String,
    max: String
  },
  data () {
    return {
      display: false,
      formattedDate: ''
    }
  },
  methods: {
    pickDate (e) {
      this.display = false
      this.$emit('input', e)
    }
  },
  watch: {
    value: {
      handler (nv) {
        if (nv) {
          const date = new Date(this.value)
          const day = date.getDate() < 10 ? `0${date.getDate()}` : date.getDate()
          const month = date.getMonth() < 9 ? `0${date.getMonth() + 1}` : date.getMonth() + 1
          const year = date.getFullYear()
          this.formattedDate = `${day}.${month}.${year}`
        } else {
          this.formattedDate = ''
        }
      }
    }
  }
}
</script>
