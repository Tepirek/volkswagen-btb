<template>
  <v-list-item>
    <v-avatar
      size="24"
      class="mr-3"
      :style="isPL(item) ? 'border: 1px solid red' : ''"
    >
      <v-img
        :src="`${countryFlags[item]}`"
      >
      </v-img>
    </v-avatar>
    {{ $t(`profile.card.language.${item}`) }}
  </v-list-item>
</template>
<script>
import { LANGUAGE_PL, COUNTRY_FLAGS } from '@/constants/settings'

export default {
  name: 'IconLanguageListItem',
  props: {
    item: String
  },
  data () {
    return {
      countryFlags: COUNTRY_FLAGS
    }
  },
  methods: {
    isPL (item) {
      return item === LANGUAGE_PL
    }
  }
}
</script>
