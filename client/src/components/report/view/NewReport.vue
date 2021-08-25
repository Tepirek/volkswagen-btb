<template>
  <v-container fluid grid-list-lg>
    <v-layout row justify-center align-center>
      <v-flex xs10 sm8 md6 lg4>
        <v-card
          class="mt-2"
          elevation="10"
        >
          <v-card-title
            class="headline"
          >
            {{ $t('report.new_report.title') }}
          </v-card-title>

          <custom-divider></custom-divider>

          <v-card-text>
            <new-report-form
              @submit="submit"
            >
            </new-report-form>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import NewReportForm from '@/components/report/components/NewReportForm'
import { mapActions, mapState } from 'vuex'
import CustomDivider from '@/components/reusable/CustomDivider'
export default {
  name: 'NewReport',
  components: { CustomDivider, NewReportForm },
  data () {
    return {
    }
  },
  computed: {
    ...mapState('report/report', {
      report: state => state.report
    })
  },
  methods: {
    ...mapActions('stepper', {
      updateStep: 'updateStep'
    }),
    ...mapActions('toolbar', {
      updateToolbarText: 'updateText'
    }),
    ...mapActions('report/report', {
      create: 'create',
      fetchOne: 'fetchOne'
    }),
    submit (data) {
      this.create({
        body_type: data.bodyType.id,
        color: data.color.id,
        pin: data.pin
      })
        .then(_ => {
          this.updateStep(1)
          this.updateToolbarText(`${this.report.body_type.name} | ${this.report.color.name} | ${this.report.pin}`)
          this.$router.push(`/report/create/${this.report.id}`)
        })
    }
  }
}
</script>
