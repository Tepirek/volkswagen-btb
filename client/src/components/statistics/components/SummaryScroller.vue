<template>
  <v-card
    elevation="10"
  >
    <v-card-title>
      {{ title }}
    </v-card-title>
    <custom-divider></custom-divider>
    <v-virtual-scroll
      :bench="benched"
      :items="items"
      height="320"
      item-height="64"
    >
      <template v-slot:default="{ item }">
        <v-list-item :key="item">
          <v-list-item-action>
            <v-btn
              fab
              small
              depressed
              color="primary"
            >
              KW{{ item }}
            </v-btn>
          </v-list-item-action>
          <v-list-item-icon class="my-auto">
            <v-icon
              class="mr-2"
            >mdi-file-pdf</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-subtitle>
              08.17.2021 - 08.17.2021
            </v-list-item-subtitle>
          </v-list-item-content>
          <v-list-item-action>
            <v-icon small>
              mdi-magnify-plus
            </v-icon>
          </v-list-item-action>
        </v-list-item>

        <v-divider></v-divider>
      </template>
    </v-virtual-scroll>
  </v-card>
</template>
<script>
import CustomDivider from '../../reusable/CustomDivider'
export default {
  name: 'SummaryScroller',
  components: { CustomDivider },
  props: {
    title: String
  },
  data: () => ({
    benched: 10
  }),
  computed: {
    items () {
      return Array.from({ length: this.length }, (k, v) => v + 1)
    },
    length () {
      return 100
    }
  }
}
</script>
