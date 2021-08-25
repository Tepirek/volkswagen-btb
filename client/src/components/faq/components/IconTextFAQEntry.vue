<template>
  <v-container
    fluid
    class="pt-0 pb-0"
  >
    <v-layout>
      <v-flex xs1 class="d-flex align-center justify-center">
        <v-icon
          class="mr-3"
          :color="iconColor"
        >
          {{ icon }}
        </v-icon>
      </v-flex>
      <v-flex xs11 class="d-flex">
        <v-container fluid>
          <span class="text-wrap">
            {{ text }}
          </span>
        </v-container>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  name: 'IconTextFAQEntry',
  props: {
    icon: String,
    iconColor: {
      type: String,
      default: 'grey darken-1'
    },
    text: String
  }
}
</script>
