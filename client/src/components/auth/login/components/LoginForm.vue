<template>
  <v-form
    ref="form"
    v-model="valid"
  >
    <v-text-field
      v-model="worker_id"
      type="text"
      autocomplete="off"
      :counter="10"
      :rules="loginRules"
      :label= "$t('auth.login.form.labels.username')"
      required
      append-icon="mdi-account"
      error-count="1"
    ></v-text-field>

    <v-text-field
      v-model="password"
      type="password"
      autocomplete="off"
      :rules="passwordRules"
      :label= "$t('auth.login.form.labels.password')"
      required
      append-icon="mdi-lock"
      error-count="1"
      color="primary"
    ></v-text-field>

    <div class="text-center">
      <v-btn
        color="primary"
        elevation="5"
        :disabled="disabled"
        @click="submit"
      >
        {{ $t('auth.login.form.login_button') }}
      </v-btn>
    </div>
  </v-form>
</template>
<script>
export default {
  name: 'LoginForm',
  data () {
    return {
      isMounted: false,
      worker_id: '',
      password: '',
      valid: true,
      loginRules: [
        v => !!v || this.$t('auth.login.form.errors.required_field.required_login')
        // v => (!!v && v.length === 10) || 'ID musi zawierać 10 znaków!'
      ],
      passwordRules: [
        v => !!v || this.$t('auth.login.form.errors.required_field.required_password')
      ]
    }
  },
  computed: {
    disabled () {
      return this.isMounted && !this.valid
    }
  },
  methods: {
    submit () {
      if (this.$refs.form.validate()) {
        this.$emit('submit', {
          worker_id: this.worker_id,
          password: this.password
        })
      }
    }
  },
  mounted () {
    this.isMounted = true
  }
}
</script>
