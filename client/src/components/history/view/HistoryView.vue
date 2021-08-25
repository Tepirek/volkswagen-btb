<template>
  <v-container fluid grid-list-lg>
    <v-layout row align-center justify-center>
      <v-flex
          class="d-flex"
          v-if="!!loadingMany"
          xs12
      >
        <v-progress-circular
          class="mx-auto mt-10"
          indeterminate
          color="white"
          :size="50"
        ></v-progress-circular>
      </v-flex>
      <v-flex xs12 sm10 md9 lg7 xl5>
        <history-timeline
          v-if="!loadingMany && logs && logs.length"
          :items="logs"
        ></history-timeline>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import HistoryTimeline from '../components/HistoryTimeline'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'HistoryView',
  components: { HistoryTimeline },
  computed: {
    ...mapState('history/history', {
      isInit: state => state.isInit,
      loadingMany: state => state.loading.many,
      logs: state => state.logs
    })
  },
  methods: {
    ...mapActions('history/history', {
      fetchLogs: 'fetchAll'
    })
  },
  mounted () {
    this.fetchLogs()
  }
}
</script>
