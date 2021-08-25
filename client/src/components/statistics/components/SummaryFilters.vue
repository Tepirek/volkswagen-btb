<template>
  <v-card>
    <v-card-title>
      {{ $t('statistics.filters.title') }}
    </v-card-title>
    <v-card-text>
      <v-form
        ref="form"
        v-model="valid"
      >
        <v-select
          :label= "$t('statistics.filters.summary_type')"
          v-model="type"
          :items="types"
          :rules="typesRules"
          required
        >
          <template v-slot:selection="{ item }">
            {{ $t(`statistics.filters.types.${item}`) }}
          </template>
          <template v-slot:item="{ item }">
            {{ $t(`statistics.filters.types.${item}`) }}
          </template>
        </v-select>
        <date-field
          v-if="!isTypeYearly"
          :label= "$t('statistics.filters.time_start')"
          :max="dateTo"
          v-model="dateFrom"
        >
        </date-field>
        <date-field
          v-if="!isTypeYearly"
          :label= "$t('statistics.filters.time_end')"
          :min="dateFrom"
          v-model="dateTo"
        >
        </date-field>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
        :disabled="disabled"
        color="primary"
        @click="applyFilters"
      >
        {{ $t('statistics.filters.find_summaries') }}
      </v-btn>
    </v-card-actions>
  </v-card>
</template>
<script>
import DateField from '../../reusable/DateField'
import { mapActions } from 'vuex'
import { TYPES, TYPE_YEARLY } from '@/constants/statistics'

export default {
  name: 'SummaryFilters',
  components: { DateField },
  data () {
    return {
      isMounted: false,
      valid: true,
      types: TYPES,
      type: '',
      dateFrom: '',
      dateTo: '',
      typesRules: [
        v => !!v || this.$t('statistics.required_field')
      ]
    }
  },
  computed: {
    disabled () {
      return this.isMounted && !this.valid
    },
    isTypeYearly () {
      return this.type === TYPE_YEARLY
    }
  },
  methods: {
    ...mapActions('summary/summary', {
      updateFiltersVisible: 'updateFiltersVisible',
      updateFilters: 'updateFilters'
    }),
    applyFilters () {
      this.updateFilters({
        type: this.type,
        date_from: this.dateFrom,
        date_to: this.dateTo
      })
      this.updateFiltersVisible(false)
    }
  },
  watch: {
    type: {
      handler (nv) {
        if (nv === TYPE_YEARLY) {
          this.dateFrom = ''
          this.dateTo = ''
        }
      }
    }
  },
  mounted () {
    this.isMounted = true
  }
}
</script>
