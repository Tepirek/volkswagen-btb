<template>
  <v-dialog
    v-model="value"
    max-width="400px"
    persistent
  >
    <v-card>
      <v-card-title
        class="
          primary
          white--text
        "
      >
        <v-icon
          color="white"
          class="mr-1"
        >
          mdi-delete
        </v-icon>
       {{ $t('point_delete_dialog.delete_point') }}
      </v-card-title>
      <v-card-text class="pa-0 pl-2">
        <v-list dense>
          <v-list-item>
            <v-list-item-icon>
              <v-icon color="primary">mdi-chart-timeline-variant</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <h4>{{ steps[data.stage ? data.stage - 1 : 0].text }}</h4>
            </v-list-item-content>
          </v-list-item>
<!--          <v-list-item>
            <v-list-item-icon>
              <v-icon color="primary">mdi-map-marker</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <h4>( x: {{ data ? ~~data.x : 0 }}, y: {{ data ? ~~data.y : 0 }} )</h4>
            </v-list-item-content>
          </v-list-item>-->
          <v-list-item>
            <v-list-item-icon>
              <v-icon color="primary">mdi-bug</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <h4>{{ data.error_type ? data.error_type.name : '' }} {{ data.inclusion_type && data.inclusion_type.name ? `(${data.inclusion_type.name})` : '' }}</h4>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-icon>
              <v-icon color="primary">mdi-clock</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <h4>{{ data ? data.created_at : '' }}</h4>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-card-text>
      <v-divider></v-divider>
      <v-card-actions>
        <v-btn
          text
          small
          @click="$emit('close')"
        >
          {{ $t('point_delete_dialog.buttons.cancel') }}
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn
          text
          small
          color="error"
          @click="$emit('confirm', data)"
        >
          {{ $t('point_delete_dialog.buttons.delete') }}
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
import { STEPS } from '../../constants'
export default {
  name: 'DeleteConfirmDialog',
  data () {
    return {
      steps: STEPS
    }
  },
  props: {
    value: Boolean,
    data: {
      type: Object,
      required: true
    }
  }
}
</script>
