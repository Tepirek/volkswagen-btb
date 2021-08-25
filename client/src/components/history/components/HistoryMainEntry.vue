<template>
<v-timeline-item
      class="mb-4"
      color="grey darken-2"
      small
      icon="mdi-pen"
    >
      <v-card
        elevation="5"
      >
        <v-card-title
          class="subtitle-1 font-weight-bold"
        >
          {{ $t(title) }}
        </v-card-title>
        <custom-divider></custom-divider>
        <v-card-text class="pa-0 pl-4 pt-2 pr-4">
          {{ description }}
        </v-card-text>
        <v-card-subtitle class="caption text-right">
          {{ date }}
        </v-card-subtitle>
      </v-card>
    </v-timeline-item>
</template>
<script>
import CustomDivider from '../../reusable/CustomDivider'
export default {
  name: 'HistoryMainEntry',
  components: { CustomDivider },
  props: {
    title: String,
    description: String,
    date: String
  }
}
</script>
