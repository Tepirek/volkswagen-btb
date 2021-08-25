<template>
  <v-app>
    <v-fade-transition>
      <router-view
        @clickAction="drawer = !drawer"
        v-if="isAuthenticated"
        name="toolbar"
      ></router-view>
    </v-fade-transition>

    <v-navigation-drawer
      v-if="isAuthenticated"
      v-model="drawer"
      app
      disable-resize-watcher
      disable-route-watcher
      width="30ch"
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            {{ user ? user.first_name : '' }} {{ user ? user.last_name : '' }}
          </v-list-item-title>
          <v-list-item-subtitle>
            ID: {{ user ? user.worker_id : '' }}
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider
        class="ml-2 mr-2 my-auto"
      ></v-divider>
      <v-list
        dense
        nav
      >
        <v-list-item-group
          v-model="selectedItem"
          color="primary"
        >
          <v-list-item
            v-for="(item, key) in items"
            :key="key"
            link
            :to="item.to"
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
                <v-list-item-title>
                  {{ item.title }}
                </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
      <template v-slot:append>
        <div class="text-center pa-4">
          <v-btn
            color="secondary"
            small
            append-icon="mdi-logout"
            @click="logout"
          >
            {{ $t('auth.logout.form.logout_button') }}
          </v-btn>
        </div>
      </template>
    </v-navigation-drawer>
    <v-main>
      <router-view name="default"/>
    </v-main>
    <notifications-snackbar>
    </notifications-snackbar>
  </v-app>
</template>

<script>

import { mapActions, mapGetters, mapState } from 'vuex'
import NotificationsSnackbar from './components/reusable/notifications/NotificationsSnackbar'

export default {
  name: 'App',
  components: { NotificationsSnackbar },
  data () {
    return {
      drawer: false,
      selectedItem: 0,
      items: [
        { id: 1, title: this.$t('nav.profile'), icon: 'mdi-account', to: '/profile' },
        { id: 2, title: this.$t('nav.new_report'), icon: 'mdi-plus', to: '/report/new' },
        { id: 3, title: this.$t('nav.my_reports'), icon: 'mdi-file-pdf', to: '/report/list' },
        { id: 4, title: this.$t('nav.statistics'), icon: 'mdi-chart-bar', to: '/statistics' },
        { id: 5, title: this.$t('nav.history'), icon: 'mdi-history', to: '/history' }
      ]
    }
  },
  computed: {
    ...mapState('toolbar', {
      toolbarText: state => state.text
    }),
    ...mapGetters('auth', {
      isAuthenticated: 'isAuthenticated'
    }),
    ...mapState('auth', {
      user: 'user'
    })
  },
  methods: {
    ...mapActions('auth', {
      logout: 'logout'
    })
  }
}
</script>
<style scoped>
  #app {
    background-color: #1976d2;
  }
</style>
