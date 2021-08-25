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
          icon="mdi-car"
          :text="$t('faq.list_report.body_type')"
        ></icon-text-f-a-q-entry>
        <icon-text-f-a-q-entry
          icon="mdi-palette"
          :text="$t('faq.list_report.color')"
        ></icon-text-f-a-q-entry>
        <icon-text-f-a-q-entry
          icon="mdi-clock"
          :text="$t('faq.list_report.create_at')"
        ></icon-text-f-a-q-entry>
        <icon-text-f-a-q-entry
          icon="mdi-clock-check"
          iconColor="success darken-1"
          :text="$t('faq.list_report.done_at')"
        ></icon-text-f-a-q-entry>
        <icon-text-f-a-q-entry
          icon="mdi-progress-wrench"
          iconColor="grey darken-1"
          :text="$t('faq.list_report.pedding')"
        ></icon-text-f-a-q-entry>
        <icon-text-f-a-q-entry
          icon="mdi-progress-check"
          iconColor="success darken-1"
          :text="$t('faq.list_report.done')"
        ></icon-text-f-a-q-entry>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>
<script>
import IconTextFAQEntry from './components/IconTextFAQEntry'

export default {
  name: 'MyReportsFAQDialog',
  components: { IconTextFAQEntry },
  props: {
    value: Boolean
  }
}
</script>
