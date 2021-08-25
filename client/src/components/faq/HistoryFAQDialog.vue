<template>
  <v-dialog
    :value="value"
    @input="$emit('input', $event)"
    persistent
    max-width="500"
    overlay-opacity="0.85"
  >
    <v-card
    >
      <v-card-title
        class="primary headline white--text"
      >
        <v-icon
          class="mr-6"
          color="white"
        >
          mdi-help-circle-outline
        </v-icon>
        <span>
          {{ $t('faq.title') }}
        </span>
        <v-spacer></v-spacer>
        <v-icon
          color="white"
          @click="$emit('input', false)"
        >
          mdi-close
        </v-icon>
      </v-card-title>
      <v-card-text class="pt-3 pb-3 pl-3 pr-3">
        <icon-text-f-a-q-entry
          icon="mdi-account"
          :text="$t('faq.history.description')"
        ></icon-text-f-a-q-entry>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>
<script>
import IconTextFAQEntry from './components/IconTextFAQEntry'

export default {
  name: 'HistoryFAQDialog',
  components: { IconTextFAQEntry },
  props: {
    value: Boolean
  }
}
</script>
