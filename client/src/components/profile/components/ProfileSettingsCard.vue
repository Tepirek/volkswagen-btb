<template>
    <v-card
      elevation="10"
      class="pt-4"
      @click="$emit('clickAction')"
    >
      <div>
        <v-layout column align-center justify-center>
          <v-icon
            :size="60"
            :color="iconColor"
          >
            {{ icon }}
          </v-icon>
          <v-flex>
            {{ text }}
          </v-flex>
        </v-layout>
      </div>
    </v-card>
</template>
<script>
export default {
  name: 'ProfileSettingsCard',
  props: {
    icon: String,
    iconColor: String,
    text: String
  },
  data () {
    return {
      display: true
    }
  }
}
</script>
