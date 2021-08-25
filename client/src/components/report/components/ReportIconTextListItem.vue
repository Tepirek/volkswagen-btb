<template>
  <v-list-item>
    <v-list-item-icon>
      <v-icon
        :color="iconColor"
      >{{ icon }}</v-icon>
    </v-list-item-icon>
    <v-list-item-content>
      {{ text }}
    </v-list-item-content>
  </v-list-item>
</template>
<script>
export default {
  name: 'ReportIconTextListItem',
  props: {
    icon: String,
    iconColor: {
      type: String,
      default: ''
    },
    text: String
  }
}
</script>
