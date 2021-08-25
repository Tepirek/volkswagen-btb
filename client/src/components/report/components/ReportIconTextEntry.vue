<template>
  <div
    class="d-flex"
  >
    <v-icon
      class="mr-2"
      color="primary"
    >
      {{ icon }}
    </v-icon>
    <p class="
      d-inline-block
      my-auto
      font-weight-bold
    ">
      {{ text }}
    </p>
  </div>
</template>
<script>
export default {
  name: 'ReportIconTextEntry',
  props: {
    icon: String,
    text: String
  }
}
</script>
