<template>
  <v-dialog
    :value="value"
    @input="$emit('input', $event)"
    persistent
    max-width="500"
    overlay-opacity="0.85"
  >
    <v-card
    >
      <v-card-title
        class="primary headline white--text"
      >
        <v-icon
          class="mr-6"
          color="white"
        >
          mdi-image-plus
        </v-icon>
        <span>
          {{ $t('statistics.new_summaries.title') }}
        </span>
        <v-spacer></v-spacer>
        <v-icon
          color="white"
          @click="$emit('input', false)"
        >
          mdi-close
        </v-icon>
      </v-card-title>
      <v-card-text class="pt-3 pb-3 pl-3 pr-3">
        <date-field
          :label= "$t('statistics.new_summaries.time_start')"
          :max="dateTo"
          v-model="dateFrom"
        >
        </date-field>
        <date-field
          :label= "$t('statistics.new_summaries.time_end')"
          :min="dateFrom"
          v-model="dateTo"
        >
        </date-field>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color="primary"
          :disabled="disabled"
          @click="createSummary"
          :loading="creationInProgress"
        >
          {{ $t('statistics.new_summaries.create_summary') }}
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
import DateField from '../../reusable/DateField'
import { mapActions } from 'vuex'

export default {
  name: 'CustomSummaryDialog',
  components: { DateField },
  props: {
    value: Boolean
  },
  data () {
    return {
      isMounted: false,
      dateFrom: '',
      dateTo: '',
      creationInProgress: false
    }
  },
  computed: {
    disabled () {
      return !!(this.isMounted && (!this.dateFrom || !this.dateTo))
    }
  },
  methods: {
    ...mapActions('summary/summary', {
      updateFiltersVisible: 'updateFiltersVisible',
      updateFilters: 'updateFilters',
      create: 'create'
    }),
    createSummary () {
      this.creationInProgress = true
      this.create({
        type: 'custom',
        date_from: this.dateFrom,
        date_to: this.dateTo
      })
        .then(_ => {
          this.dateFrom = ''
          this.dateTo = ''
          this.creationInProgress = false
          this.updateFilters({
            type: 'custom',
            date_from: null,
            date_to: null
          })
            .then(_ => {
              this.updateFiltersVisible(false)
            })
          this.$emit('input', false)
        })
    }
  },
  mounted () {
    this.isMounted = true
  }
}
</script>
