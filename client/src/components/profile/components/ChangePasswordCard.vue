<template>
  <v-card>
    <v-card-title
      class="subtitle-1 font-weight-bold"
    >
      <v-icon
        class="mr-2"
        color="amber darken-3"
      >mdi-lock-open-outline</v-icon>
      {{ $t('profile.card.settings.password') }}
    </v-card-title>
    <v-card-text>
      <v-form
        ref="form"
      >
        <v-text-field
          type="password"
          append-icon="mdi-lock"
          :label="$t('profile.card.password.current')"
        ></v-text-field>
        <v-text-field
          type="password"
          append-icon="mdi-lock"
          :label="$t('profile.card.password.new')"
        ></v-text-field>
        <v-text-field
          type="password"
          append-icon="mdi-lock"
          :label="$t('profile.card.password.repeat')"
        ></v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
        color="success darken-1"
      >
        {{ $t('profile.card.confirm') }}
      </v-btn>
    </v-card-actions>
  </v-card>
</template>
<script>
export default {
  name: 'ChangePasswordCard'
}
</script>
