<template>
  <v-app-bar
    app
    color="primary"
    dark
  >
    <v-app-bar-nav-icon @click="$emit('clickAction')"></v-app-bar-nav-icon>
    <v-toolbar-title>{{ toolbarText }}</v-toolbar-title>
  </v-app-bar>
</template>
<script>
export default {
  name: 'DefaultToolbar'
}
</script>
