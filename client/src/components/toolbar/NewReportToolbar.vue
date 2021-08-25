<template>
  <v-app-bar
    app
    color="primary"
    dark
  >
    <v-app-bar-nav-icon @click="$emit('clickAction')"></v-app-bar-nav-icon>
    <v-toolbar-title>{{ $t('report.toolbar.new') }}</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-icon
      @click="faqDialog = true"
    >
      mdi-help-circle-outline
    </v-icon>
    <new-report-f-a-q-dialog
      v-model="faqDialog"
    ></new-report-f-a-q-dialog>
  </v-app-bar>
</template>
<script>
import NewReportFAQDialog from '../faq/NewReportFAQDialog'

export default {
  name: 'NewReportToolbar',
  components: { NewReportFAQDialog },
  data () {
    return {
      faqDialog: false
    }
  }
}
</script>
