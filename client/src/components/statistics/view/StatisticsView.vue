<template>
  <v-container fluid grid-list-lg>
    <v-expand-transition>
      <v-layout
        v-show="filtersVisible"
        row wrap align-center justify-center>
        <v-flex xs11 sm9 md7 lg5>
          <summary-filters
          ></summary-filters>
        </v-flex>
      </v-layout>
    </v-expand-transition>
    <v-layout row wrap>
      <v-progress-circular
        v-if="loadingMany"
        indeterminate
        color="white"
        :size="50"
        class="mx-auto mt-10"
      ></v-progress-circular>
    <v-flex
      class="xs12 sm6 md4 lg3"
      v-for="item in summaries"
      :key="item.id"
    >
      <v-card>
        <v-card-title class="pb-0">
          Podsumowanie: #{{ item.id }}
          <v-spacer></v-spacer>
          <v-btn
            :href="item.file"
            target="_blank"
            small
            fab
          >
            <v-icon
              color="red darken-3"
            >mdi-file-pdf</v-icon>
          </v-btn>
        </v-card-title>
        <v-card-text class="pa-0 pl-4">
          <v-list dense>
            <icon-text-list-item
              icon="mdi-calendar-arrow-right"
              :text="item.date_start"
            ></icon-text-list-item>
            <icon-text-list-item
              icon="mdi-calendar-arrow-left"
              :text="item.date_end"
            ></icon-text-list-item>
            <icon-text-list-item
              icon="mdi-calendar-range"
              :text="$t(`statistics.filters.type.${item.type}`)"
            ></icon-text-list-item>
          </v-list>
        </v-card-text>
      </v-card>
    </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import SummaryFilters from '../components/SummaryFilters'
import { mapActions, mapState } from 'vuex'
import IconTextListItem from '@/components/reusable/IconTextListItem'

export default {
  name: 'StatisticsView',
  components: { IconTextListItem, SummaryFilters },
  data () {
    return {
    }
  },
  computed: {
    ...mapState('summary/summary', {
      loadingMany: state => state.loading.many,
      summaries: state => state.summaries,
      filters: state => state.filters,
      filtersVisible: state => state.filtersVisible
    })
  },
  methods: {
    ...mapActions('summary/summary', {
      fetchAll: 'fetchAll'
    })
  },
  watch: {
    filters: {
      handler (nv) {
        this.fetchAll()
      }
    }
  }
}
</script>
