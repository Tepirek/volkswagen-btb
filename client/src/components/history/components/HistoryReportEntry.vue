<template>
  <v-timeline-item
    class="mb-4"
    :color="title === 'report_updated' ? 'success darken-1' : 'grey darken-2'"
    small
    :icon="title === 'report_updated' ? 'mdi-check-bold' : 'mdi-pen'"
  >
    <v-card
      elevation="5"
    >
      <v-card-title
        class="subtitle-2 font-weight-bold"
      >
        {{ $t(`history.actions.${title}`) }} #{{ id }}
      </v-card-title>
      <v-card-subtitle class="caption text-right">
        {{ date }}
      </v-card-subtitle>
    </v-card>
  </v-timeline-item>
</template>
<script>
export default {
  name: 'HistoryReportEntry',
  props: {
    title: String,
    id: Number,
    date: String
  }
}
</script>
