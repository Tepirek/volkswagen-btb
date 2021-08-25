<template>
  <v-app-bar
    app
    color="primary"
    dark
  >
    <v-app-bar-nav-icon @click="$emit('clickAction')"></v-app-bar-nav-icon>
    <v-toolbar-title>{{ $t('history.toolbar.title') }}</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-icon
      @click="faqDialog = true"
    >
      mdi-help-circle-outline
    </v-icon>
    <history-f-a-q-dialog
      v-model="faqDialog"
    ></history-f-a-q-dialog>
  </v-app-bar>
</template>
<script>
import HistoryFAQDialog from '../faq/HistoryFAQDialog'

export default {
  name: 'HistoryToolbar',
  components: { HistoryFAQDialog },
  data () {
    return {
      faqDialog: false
    }
  }
}
</script>
