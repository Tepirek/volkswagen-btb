<template>
  <v-snackbar
    v-model="visible"
    :timeout="timeout"
    color="white"
    :elevation="10"
  >
    <v-layout row wrap>
      <v-flex shrink class="ml-2">
        <v-icon
          :color="data ? data.color : ''"
          class="mr-2"
        >
          {{ data ? data.icon : '' }}
        </v-icon>
      </v-flex>
      <v-flex grow class="d-flex">
        <span class="my-auto black--text subtitle-2">
          {{ $t(data ? data.text : '') }}
        </span>
      </v-flex>
    </v-layout>
    <template v-slot:action="{ attrs }">
      <v-icon
        v-bind="attrs"
        color="black"
        @click="visible = false"
      >
        mdi-close
      </v-icon>
    </template>
  </v-snackbar>
</template>
<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'NotificationsSnackbar',
  props: {
    timeout: {
      type: Number,
      default: 3000
    }
  },
  computed: {
    visible: {
      ...mapState('notification/snackbar', {
        get: state => state.visible
      }),
      ...mapActions('notification/snackbar', {
        set: 'updateVisible'
      })
    },
    ...mapState('notification/snackbar', {
      data: state => state.data,
      queue: state => state.queue
    })
  },
  methods: {
    ...mapActions('notification/snackbar', {
      pop: 'pop'
    })
  },
  watch: {
    visible: {
      handler (nv) {
        if (!nv) {
          this.$nextTick(() => this.pop())
        }
      }
    }
  }
}
</script>
