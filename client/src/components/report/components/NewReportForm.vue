<template>
  <v-form
    ref="form"
    v-model="valid"
  >
    <select-autocomplete
      :loading="bodyTypeLoading"
      :items="bodyTypes"
      :label= "$t('report.new_report.labels.body_type')"
      icon="mdi-car"
      :rules="[
        v => !!v || this.$t('report.new_report.required_field.required_body_type')
      ]"
      search="name"
      v-model="bodyType"
    >
    </select-autocomplete>
    <select-autocomplete
      :loading="colorLoading"
      :items="colors"
      :label= "$t('report.new_report.labels.color')"
      icon="mdi-palette"
      :rules="[
        v => !!v || this.$t('report.new_report.required_field.required_color_type')
      ]"
      search="name"
      v-model="color"
    >
    </select-autocomplete>
    <v-text-field
      type="text"
      error-count="1"
      :rules="[(v) => !!v || this.$t('report.new_report.required_field.required_color_type')]"
      :label= "$t('report.new_report.labels.pin')"
      append-icon="mdi-numeric"
      v-model="pin"
    >
    </v-text-field>
    <div class="text-center">
      <v-btn
        color="primary"
        elevation="5"
        :disabled="disabled"
        @click="submit"
      >
        {{ $t('report.new_report.continue')}}
      </v-btn>
    </div>
  </v-form>
</template>
<script>
import SelectAutocomplete from '@/components/reusable/SelectAutocomplete'
import { mapActions, mapState } from 'vuex'
export default {
  name: 'NewReportForm',
  components: {
    SelectAutocomplete
  },
  data () {
    return {
      isMounted: false,
      valid: true,
      bodyType: null,
      color: null,
      pin: ''
    }
  },
  computed: {
    ...mapState('bodyType', {
      bodyTypeLoading: state => state.loading,
      bodyTypes: state => state.bodyTypes
    }),
    ...mapState('color', {
      colorLoading: state => state.loading,
      colors: state => state.colors
    }),
    disabled () {
      return this.isMounted && !this.valid
    }
  },
  methods: {
    ...mapActions('bodyType', {
      fetchAllBodyTypes: 'fetchAll'
    }),
    ...mapActions('color', {
      fetchAllColors: 'fetchAll'
    }),
    submit () {
      if (this.$refs.form.validate()) {
        this.$emit('submit', {
          bodyType: this.bodyType,
          color: this.color,
          pin: this.pin
        })
      }
    }
  },
  mounted () {
    this.isMounted = true
    this.fetchAllBodyTypes()
    this.fetchAllColors()
  }
}
</script>
