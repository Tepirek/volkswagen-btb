<template>
  <v-tooltip
    left
  >
    <template v-slot:activator="{ on, attrs }">
      <v-icon
        :color="iconColor"
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
  name: 'TooltipLeft',
  props: {
    icon: String,
    iconColor: {
      type: String,
      default: 'black'
    },
    text: String,
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
