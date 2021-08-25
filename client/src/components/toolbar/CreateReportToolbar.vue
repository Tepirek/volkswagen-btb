<template>
  <v-app-bar
    app
    color="primary"
    dark
  >
    <v-app-bar-nav-icon @click="$emit('clickAction')"></v-app-bar-nav-icon>
    <v-toolbar-title
      v-if="isInit"
      class="d-flex"
    >
      <v-icon class="mr-1 my-auto">
        mdi-pen
      </v-icon>
        {{ report.body_type.name }} /
        {{ report.color.name }} /
        {{ report.pin }}
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-icon
      @click="faqDialog = true"
    >
      mdi-help-circle-outline
    </v-icon>
    <create-report-f-a-q-dialog
      v-model="faqDialog"
    ></create-report-f-a-q-dialog>
  </v-app-bar>
</template>
<script>
import { mapState } from 'vuex'
import CreateReportFAQDialog from '../faq/CreateReportFAQDialog'

export default {
  name: 'NewReportToolbar',
  components: { CreateReportFAQDialog },
  data () {
    return {
      faqDialog: false
    }
  },
  computed: {
    ...mapState('report/report', {
      isInit: state => state.isInit,
      loading: state => state.loading,
      report: state => state.report
    })
  }
}
</script>
