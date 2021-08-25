<template>
  <v-container fluid fill-height>
    <v-layout column align-center>
      <v-progress-circular
        v-if="!isInit"
        indeterminate
        color="white"
        :size="50"
        class="my-auto"
      ></v-progress-circular>
      <v-fade-transition>
        <v-stepper
          v-if="isInit"
          v-model="stage"
          class="d-flex flex-column fill-height"
          width="100%"
        >
          <v-stepper-header>
            <template v-for="(step, key) in steps">
              <v-stepper-step
                :key="key"
                :step="key + 1"
                :complete="stage > key + 1"
              >
                {{ step.text }}
              </v-stepper-step>
              <v-divider
                :key="`step-${key + 1}`"
                v-if="key !== steps.length - 1"
              ></v-divider>
            </template>
          </v-stepper-header>
          <custom-divider></custom-divider>
          <editor
            v-if="stage < 5"
          ></editor>
          <report-summary
            v-if="stage === 5"
            parent="create"
          ></report-summary>
        </v-stepper>
      </v-fade-transition>
    </v-layout>
  </v-container>
</template>
<script>
import Editor from '@/components/report/components/Editor'
import { mapActions, mapState } from 'vuex'
import CustomDivider from '@/components/reusable/CustomDivider'
import ReportSummary from '../components/ReportSummary'
export default {
  name: 'CreateReport',
  components: { ReportSummary, CustomDivider, Editor },
  props: {
  },
  data () {
    return {
      steps: [
        {
          id: 1,
          text: 'VBH/KTL'
        },
        {
          id: 2,
          text: 'PCV'
        },
        {
          id: 3,
          text: 'FL'
        },
        {
          id: 4,
          text: 'BC/CC'
        },
        {
          id: 5,
          text: this.$t('report.new_report.summary')
        }
      ]
    }
  },
  computed: {
    ...mapState('report/report', {
      isInit: state => state.isInit,
      loading: state => state.loading,
      report: state => state.report
    }),
    ...mapState('stepper', {
      stage: state => state.step
    })
  },
  methods: {
    ...mapActions('report/report', {
      fetchOne: 'fetchOne'
    })
  },
  mounted () {
    if (!this.report.id) {
      this.fetchOne(this.$route.params.slug)
    }
  }
}
</script>
<style>
 .v-stepper__wrapper {
   width: 100% !important;
 }
</style>
