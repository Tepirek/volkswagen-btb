<template>
  <v-form
    ref="form"
    v-model="valid"
  >
    <select-autocomplete
      :loading="errorTypesLoading"
      :items="errorTypes"
      :label= "$t('report.bug_dialog.labels.error_type')"
      icon="mdi-alert-circle-outline"
      :rules="[
        v => !!v || this.$t('report.bug_dialog.required_field.required_error_type')
      ]"
      search="name"
      v-model="errorType"
    >
    </select-autocomplete>
    <select-autocomplete
      v-if="errorType && errorType.name === 'Wtracenia'"
      :loading="inclusionTypesLoading"
      :items="inclusionTypes"
      :label= "$t('report.bug_dialog.labels.inclusion_type')"
      icon="mdi-alert-circle-outline"
      :rules="[
        v => !!v || this.$t('report.bug_dialog.required_field.required_inclusion_type')
      ]"
      search="name"
      v-model="inclusionType"
    >
    </select-autocomplete>
    <div class="text-center">
      <v-btn
        color="primary"
        elevation="5"
        :disabled="disabled"
        @click="submit"
      >
        {{ $t('report.bug_dialog.continue') }}
      </v-btn>
    </div>
  </v-form>
</template>
<script>
import { mapActions, mapState } from 'vuex'
import SelectAutocomplete from '@/components/reusable/SelectAutocomplete'

export default {
  name: 'BugDialogForm',
  components: {
    SelectAutocomplete
  },
  data () {
    return {
      isMounted: false,
      valid: true
    }
  },
  computed: {
    ...mapState('errorType', {
      errorTypesLoading: state => state.loading,
      errorTypes: state => state.errorTypes
    }),
    ...mapState('inclusionType', {
      inclusionTypesLoading: state => state.loading,
      inclusionTypes: state => state.inclusionTypes
    }),
    errorType: {
      ...mapState('errorType', {
        get: state => state.errorType
      }),
      set (v) {
        this.updateErrorType(v ? { ...v } : null)
      }
    },
    inclusionType: {
      ...mapState('inclusionType', {
        get: state => state.inclusionType
      }),
      set (v) {
        this.updateInclusionType(v ? { ...v } : null)
      }
    },
    disabled () {
      return this.isMounted && !this.valid
    }
  },
  methods: {
    ...mapActions('errorType', {
      fetchAllErrorTypes: 'fetchAll',
      updateErrorType: 'updateErrorType'
    }),
    ...mapActions('inclusionType', {
      fetchAllInclusionTypes: 'fetchAll',
      updateInclusionType: 'updateInclusionType'
    }),
    submit () {
      if (this.$refs.form.validate()) {
        this.$emit('submit', {
          errorType: this.errorType,
          inclusionType: this.inclusionType
        })
      }
    }
  },
  mounted () {
    this.isMounted = true
    this.fetchAllErrorTypes()
    this.fetchAllInclusionTypes()
  },
  watch: {
    errorType: function (value) {
      if (!value) {
        this.inclusionType = null
      } else if (value && value.name.localeCompare('wtracenia') !== 0) {
        this.inclusionType = null
      }
    }
  }
}
</script>
