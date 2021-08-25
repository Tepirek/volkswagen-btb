<template>
  <v-app-bar
    app
    color="primary"
    dark
  >
    <v-app-bar-nav-icon @click="$emit('clickAction')"></v-app-bar-nav-icon>
    <v-toolbar-title>{{ $t('report.toolbar.my_reports') }}</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-icon
      @click="faqDialog = true"
    >
      mdi-help-circle-outline
    </v-icon>
    <my-reports-f-a-q-dialog
      v-model="faqDialog"
    ></my-reports-f-a-q-dialog>
  </v-app-bar>
</template>
<script>
import MyReportsFAQDialog from '../faq/MyReportsFAQDialog'

export default {
  name: 'DefaultToolbar',
  components: { MyReportsFAQDialog },
  data () {
    return {
      faqDialog: false
    }
  }
}
</script>
