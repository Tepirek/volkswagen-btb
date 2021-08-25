<template>
  <v-card>
    <v-card-text>
      <v-layout row wrap>
        <v-flex
          xs12 sm8 lg9
        >
          <v-flex
            class="d-flex headline black--text"
          >
            {{ user ? user.first_name : '' }}
            {{ user ? user.last_name : '' }}
            <v-spacer></v-spacer>
            <v-avatar
              size="100"
              style="position: absolute; top: 20px; right: 20px"
              v-show="!!$vuetify.breakpoint.xsOnly"
            >
              <img
               src="https://img.freepik.com/darmowe-wektory/awatar-postaci-biznesmen-na-bialym-tle_24877-60111.jpg?size=338&ext=jpg"
              >
            </v-avatar>
          </v-flex>
          <v-list dense>
            <icon-text-list-item
              icon="mdi-account"
              :text="user ? user.worker_id : ''"
            ></icon-text-list-item>
            <icon-text-list-item
              icon="mdi-phone"
              text="+48 123 456 789"
            ></icon-text-list-item>
            <icon-text-list-item
              icon="mdi-email"
              :text="email"
            ></icon-text-list-item>
          </v-list>
        </v-flex>
        <v-flex
          xs12 sm4 lg3
        >
          <v-img
            v-show="!$vuetify.breakpoint.xsOnly"
            width="100%"
            :aspect-ratio="1/1"
            src="https://img.freepik.com/darmowe-wektory/awatar-postaci-biznesmen-na-bialym-tle_24877-60111.jpg?size=338&ext=jpg"
          ></v-img>
        </v-flex>
      </v-layout>
    </v-card-text>
  </v-card>
</template>
<script>
import IconTextListItem from '../../reusable/IconTextListItem'
export default {
  name: 'ProfileInfoCard',
  components: { IconTextListItem },
  props: {
    user: Object
  },
  computed: {
    email () {
      const firstName = this.user ? this.user.first_name : ''
      const lastName = this.user ? this.user.last_name : ''
      return `${firstName}.${lastName}@volkswagen.com`
    }
  }
}
</script>
