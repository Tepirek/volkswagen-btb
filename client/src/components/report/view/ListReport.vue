<template>
  <v-container
    fluid
    grid-list-lg
  >
    <v-layout
      row
    >
    <v-progress-circular
      v-if="setLoadingMany"
      indeterminate
      color="white"
      :size="50"
      class="mx-auto mt-10"
    ></v-progress-circular>
    <v-flex
      class="xs12 sm6 md4 lg3"
      v-for="item in reports"
      :key="item.id"
    >
      <v-card>
        <v-card-title class="pb-0">
         {{ $t('report.report_list.report_number') }}{{ item.id }}
          <v-spacer></v-spacer>
          <v-icon
            :color="item.state === 'done' ? 'success darken-1' : 'grey darken-1'"
          >
            {{ item.state === 'done' ? 'mdi-progress-check' : 'mdi-progress-wrench' }}
          </v-icon>
        </v-card-title>
        <v-card-text class="pa-0 pl-4">
          <v-list dense>
            <report-icon-text-list-item
              icon="mdi-car"
              :text="item.body_type.name"
            ></report-icon-text-list-item>
            <report-icon-text-list-item
              icon="mdi-palette"
              :text="item.color.name"
            ></report-icon-text-list-item>
            <report-icon-text-list-item
              v-if="item.state !== 'done'"
              icon="mdi-clock"
              :text="item.created_at"
            ></report-icon-text-list-item>
            <report-icon-text-list-item
              v-if="item.state === 'done'"
              icon="mdi-clock-check"
              iconColor="success darken-1"
              :text="item.sent_at"
            ></report-icon-text-list-item>
          </v-list>
        </v-card-text>
        <v-card-actions class="pt-0">
          <v-spacer></v-spacer>
          <v-btn
            v-if="item.state !== 'done'"
            small
            elevation="0"
            :href="`/report/create/${item.id}`"
          >
            {{ $t('report.report_list.buttons.edit') }}
          </v-btn>
          <v-btn
            small
            class="white--text amber darken-2"
            @click="showSummary(item.id)"
          >
            {{ $t('report.report_list.buttons.preview') }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
    <v-dialog
      v-model="display"
      persistent
      overlay-opacity="0.85"
      max-width="1000px"
    >
      <report-summary
        parent="list"
        @closeAction="closeSummary"
      ></report-summary>
    </v-dialog>
  </v-container>
</template>
<script>
import { mapActions, mapState } from 'vuex'
import ReportSummary from '../components/ReportSummary'
import ReportIconTextListItem from '../components/ReportIconTextListItem'

export default {
  name: 'ListReport',
  components: { ReportIconTextListItem, ReportSummary },
  data () {
    return {
      display: false
    }
  },
  computed: {
    ...mapState('report/report', {
      setLoadingOne: state => state.loading.one,
      setLoadingMany: state => state.loading.many,
      reports: state => state.reports
    })
  },
  methods: {
    ...mapActions('report/report', {
      fetchAll: 'fetchAll',
      fetchOne: 'fetchOne'
    }),
    showSummary (id) {
      this.display = true
      this.fetchOne(id)
    },
    closeSummary () {
      this.display = false
    }
  },
  mounted () {
    this.fetchAll()
  }
}
</script>
