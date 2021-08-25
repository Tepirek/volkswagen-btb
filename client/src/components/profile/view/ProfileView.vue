<template>
  <v-container fluid grid-list-lg>
    <v-layout row align-center justify-center>
      <v-flex xs11 sm10 md8 lg6>
        <profile-info-card
          :user="user"
        ></profile-info-card>
      </v-flex>
    </v-layout>
    <v-layout row align-center justify-center>
      <v-flex xs11 sm10 md8 lg6 class="d-flex pr-0 pl-0">
        <v-flex xs6 class="pt-0">
          <profile-settings-card
            icon="mdi-lock-open-outline"
            iconColor="amber darken-3"
            :text="$t('profile.card.settings.password')"
            @clickAction="togglePasswordCard"
          ></profile-settings-card>
        </v-flex>
        <v-flex xs6 class="pt-0">
          <profile-settings-card
            icon="mdi-translate"
            iconColor="teal"
            :text="$t('profile.card.settings.language')"
            @clickAction="toggleLanguageCard"
          ></profile-settings-card>
        </v-flex>
      </v-flex>
    </v-layout>
    <v-expand-transition>
      <v-layout
        v-show="passwordCardDisplay && !translationCardDisplay"
        row align-center justify-center>
        <v-flex xs11 sm10 md8 lg6>
          <change-password-card>
          </change-password-card>
        </v-flex>
      </v-layout>
    </v-expand-transition>
    <v-expand-transition>
      <v-layout
        v-show="translationCardDisplay && !passwordCardDisplay"
        row align-center justify-center>
        <v-flex xs11 sm10 md8 lg6>
          <change-language-card>
          </change-language-card>
        </v-flex>
      </v-layout>
    </v-expand-transition>
  </v-container>
</template>
<script>
import { mapState } from 'vuex'
import ProfileInfoCard from '../components/ProfileInfoCard'
import ProfileSettingsCard from '../components/ProfileSettingsCard'
import ChangePasswordCard from '../components/ChangePasswordCard'
import ChangeLanguageCard from '../components/ChangeLanguageCard'

export default {
  name: 'ProfileView',
  components: { ChangeLanguageCard, ChangePasswordCard, ProfileSettingsCard, ProfileInfoCard },
  data () {
    return {
      passwordCardDisplay: false,
      translationCardDisplay: false
    }
  },
  computed: {
    ...mapState('auth', {
      user: state => state.user
    })
  },
  methods: {
    togglePasswordCard () {
      this.passwordCardDisplay = !this.passwordCardDisplay
      this.translationCardDisplay = false
    },
    toggleLanguageCard () {
      this.translationCardDisplay = !this.translationCardDisplay
      this.passwordCardDisplay = false
    }
  }
}
</script>
