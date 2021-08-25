<template>
  <v-container fluid fill-height>
    <v-layout row align-center justify-center>
      <v-flex xs10 sm7 md6 lg4>
        <v-card
          elevation="10"
        >
          <v-card-title>
            {{ $t('auth.login.form.title') }}
          </v-card-title>
          <v-divider class="ml-3 mr-3 my-auto"></v-divider>

          <v-card-text>
            <login-form
              @submit="submit"
            >
            </login-form>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import LoginForm from '@/components/auth/login/components/LoginForm'
import { mapActions } from 'vuex'

export default {
  name: 'Login',
  components: {
    LoginForm
  },
  methods: {
    ...mapActions('auth', {
      login: 'login'
    }),
    submit (data) {
      this.login(data)
    }
  }
}
</script>

<style>

</style>
