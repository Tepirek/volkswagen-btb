<template>
  <v-card>
    <v-card-title
      class="subtitle-1 font-weight-bold"
    >
      <v-icon
        class="mr-2"
        color="teal"
      >mdi-translate</v-icon>
      {{ $t('profile.card.settings.language') }}
    </v-card-title>
    <v-card-text>
      <v-form
        ref="form"
      >
        <v-select
          v-model="language"
          :label="$t('profile.card.language.label')"
          :items="languages"
        >
          <template v-slot:selection="{ item }">
            <icon-language-list-item
              :item="item"
            ></icon-language-list-item>
          </template>
          <template v-slot:item="{ item }">
            <icon-language-list-item
              :item="item"
            ></icon-language-list-item>
          </template>
        </v-select>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
        color="success darken-1"
        @click="changeLanguage"
      >
        {{ $t('profile.card.confirm') }}
      </v-btn>
    </v-card-actions>
  </v-card>
</template>
<script>
import { LANGUAGES } from '@/constants/settings'
import IconLanguageListItem from './IconLanguageListItem'
import LS from '@/services/localStorage'

export default {
  name: 'ChangeLanguageCard',
  components: { IconLanguageListItem },
  data () {
    return {
      languages: LANGUAGES,
      language: JSON.parse(LS.get('settings')).lang
    }
  },
  methods: {
    changeLanguage () {
      const settings = JSON.parse(LS.get('settings'))
      settings.lang = this.language || settings.lang
      LS.set('settings', JSON.stringify(settings))
      this.$router.go()
    }
  }
}
</script>
