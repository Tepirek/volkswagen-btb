<template>
  <v-timeline
    dense
  >
    <template
      v-for="(item, key) in items"
    >
      <history-settings-entry
        v-if="item.type === 'report'"
        :key="key"
        :title="item.action.title"
        :id="item.reference"
        :date="item.created_at"
      >
      </history-settings-entry>
      <history-summary-entry
        v-else-if="item.type === 'summary'"
        :key="key"
        :title="item.action.title"
        :id="item.reference"
        :date="item.created_at"
      ></history-summary-entry>
    </template>
  </v-timeline>
</template>
<script>
import HistorySettingsEntry from './HistoryReportEntry'
import HistorySummaryEntry from './HistorySummaryEntry'

export default {
  name: 'HistoryTimeline',
  components: { HistorySummaryEntry, HistorySettingsEntry },
  props: {
    items: Array
  }
}
</script>
