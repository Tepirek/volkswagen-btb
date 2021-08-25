<template>
  <v-app-bar
    app
    color="primary"
    dark
  >
    <v-app-bar-nav-icon @click="$emit('clickAction')"></v-app-bar-nav-icon>
    <v-toolbar-title>{{ $t('statistics.title') }}</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-icon
      @click="customSummaryDialog = true"
      class="mr-3"
    >
      mdi-image-plus
    </v-icon>
    <v-icon
      @click="toggleFilters"
      class="mr-3"
    >
      {{ filtersVisible ? 'mdi-filter-minus-outline' : 'mdi-filter-plus-outline' }}
    </v-icon>
    <v-icon
      @click="faqDialog = true"
    >
      mdi-help-circle-outline
    </v-icon>
    <custom-summary-dialog
      v-model="customSummaryDialog"
    ></custom-summary-dialog>
    <statistics-f-a-q-dialog
      v-model="faqDialog"
    ></statistics-f-a-q-dialog>
  </v-app-bar>
</template>
<script>
import { mapActions, mapState } from 'vuex'
import StatisticsFAQDialog from '../faq/StatisticsFAQDialog'
import CustomSummaryDialog from '../statistics/components/CustomSummaryDialog'

export default {
  name: 'DefaultToolbar',
  components: { CustomSummaryDialog, StatisticsFAQDialog },
  data () {
    return {
      faqDialog: false,
      customSummaryDialog: false
    }
  },
  computed: {
    ...mapState('summary/summary', {
      filtersVisible: state => state.filtersVisible
    })
  },
  methods: {
    ...mapActions('summary/summary', {
      updateFiltersVisible: 'updateFiltersVisible'
    }),
    toggleFilters () {
      this.updateFiltersVisible(!this.filtersVisible)
    }
  }
}
</script>
