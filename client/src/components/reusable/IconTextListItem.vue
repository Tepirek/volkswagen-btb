<template>
  <v-list-item>
    <v-list-item-icon>
      <v-icon>{{ icon }}</v-icon>
    </v-list-item-icon>
    <v-list-item-content>
      {{ text }}
    </v-list-item-content>
  </v-list-item>
</template>
<script>
export default {
  name: 'IconTextListItem',
  props: {
    icon: String,
    text: String
  }
}
</script>
