<template>
  <v-app-bar
    app
    color="primary"
    dark
  >
    <v-app-bar-nav-icon @click="$emit('clickAction')"></v-app-bar-nav-icon>
    <v-toolbar-title>{{ $t('profile.toolbar.title') }}</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-icon
      @click="faqDialog = true"
    >
      mdi-help-circle-outline
    </v-icon>
    <profile-f-a-q-dialog
      v-model="faqDialog"
    ></profile-f-a-q-dialog>
  </v-app-bar>
</template>
<script>
import ProfileFAQDialog from '../faq/ProfileFAQDialog'

export default {
  name: 'DefaultToolbar',
  components: { ProfileFAQDialog },
  data () {
    return {
      faqDialog: false
    }
  }
}
</script>
