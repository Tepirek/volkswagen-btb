<template>
  <v-tooltip
    top
  >
    <template v-slot:activator="{ on, attrs }">
      <v-icon
        :color="color"
        v-bind="attrs"
        v-on="on"
        v-show="show"
        @click="$emit('click')"
        >
        {{ icon }}
      </v-icon>
    </template>
    <span>
      {{ text }}
    </span>
  </v-tooltip>
</template>
<script>
export default {
  name: 'TooltipTop',
  props: {
    icon: String,
    text: String,
    color: {
      type: String,
      default: 'black'
    },
    show: {
      type: Boolean,
      default: true
    }
  },
  data () {
    return {
    }
  }
}
</script>
