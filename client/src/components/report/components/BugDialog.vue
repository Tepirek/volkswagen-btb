<template>
  <v-dialog
    v-model="display"
    max-width="600px"
    persistent
  >
    <v-card>
      <v-card-title
        class="headline"
      >
        {{ $t('report.bug_dialog.title') }}
      </v-card-title>
      <custom-divider></custom-divider>
      <v-card-text>
        <bug-dialog-form
          @submit="submit"
        >
        </bug-dialog-form>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>
<script>
import CustomDivider from '@/components/reusable/CustomDivider'
import BugDialogForm from '@/components/report/components/BugDialogForm'
import { mapActions, mapState } from 'vuex'
export default {
  name: 'BugDialog',
  components: { BugDialogForm, CustomDivider },
  data () {
    return {
    }
  },
  computed: {
    ...mapState('stepper', {
      display: state => state.errorDialogVisible
    })
  },
  methods: {
    ...mapActions('stepper', {
      updateErrorDialogVisible: 'updateErrorDialogVisible'
    }),
    submit (data) {
      this.updateErrorDialogVisible(false)
      this.$emit('clickAction')
    }
  }
}
</script>
