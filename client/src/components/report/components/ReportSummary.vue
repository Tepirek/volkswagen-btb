<template>
  <v-layout column align-center justify-center fill-height>
    <v-card
      class="d-flex flex-column fill-height"
      width="100%"
    >
      <v-flex shrink>
       <v-card-title
         :class="parent ==='list' ? 'primary white--text' : ''"
       >
        {{ $t('report.summary.report_number') }}{{ report.id }}
         <v-spacer></v-spacer>
         <v-icon
          class="white--text"
          v-if="parent === 'list'"
          @click="closeAction"
         >mdi-close</v-icon>
      </v-card-title>
      </v-flex>
      <v-flex shrink>
        <custom-divider></custom-divider>
      </v-flex>
      <v-flex grow>
        <v-card-text>
          <span class="subtitle-1 font-weight-bold">{{ $t('report.summary.base_info') }}</span>
          <v-container fluid grid-list-lg>
            <v-layout
              row wrap
            >
              <v-flex xs6 md4 class="d-flex align-center">
                <report-icon-text-entry
                  icon="mdi-car"
                  :text="report && report.body_type ? report.body_type.name : ''"
                ></report-icon-text-entry>
              </v-flex>
              <v-flex xs6 md4 class="d-flex align-center">
                <report-icon-text-entry
                  icon="mdi-palette"
                  :text="report && report.color ? report.color.name : ''"
                ></report-icon-text-entry>
              </v-flex>
              <v-flex xs12 sm6 md4 class="d-flex align-center">
                <report-icon-text-entry
                  icon="mdi-numeric"
                  :text="report.pin"
                ></report-icon-text-entry>
              </v-flex>
              <v-flex xs12 sm6 md4 class="d-flex align-center">
                <report-icon-text-entry
                  icon="mdi-account"
                  :text="workerData"
                ></report-icon-text-entry>
              </v-flex>
              <v-flex xs6 md4 class="d-flex align-center">
                <report-icon-text-entry
                  icon="mdi-clock"
                  :text="report.created_at"
                ></report-icon-text-entry>
              </v-flex>
              <v-flex xs6 md4 class="d-flex align-center">
                <report-icon-text-entry
                  icon="mdi-clock-check"
                  :text="report.sent_at ? report.sent_at : $t('report.summary.not_sended') "
                ></report-icon-text-entry>
              </v-flex>
            </v-layout>
          </v-container>
          <v-divider class="mt-4 mb-4"></v-divider>
          <span class="subtitle-1 font-weight-bold">{{ $t('report.summary.checked_errors') }}</span>
          <v-expansion-panels
            focusable
            inset
            class="mt-4"
            v-model="opened"
          >
            <v-expansion-panel
              v-for="(item, key) in steps"
              :key="key"
            >
              <v-expansion-panel-header
                color="primary"
                class="white--text"
              >
                {{ item.text }}
                <template v-slot:actions>
                  <v-icon color="white">
                    $expand
                  </v-icon>
                </template>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-container fluid grid-list-lg>
                  <v-layout row wrap>
                    <v-flex
                      class="
                        d-flex
                        align-center
                        xs12
                        sm6
                        md4
                        lg3
                        xl2
                      "
                      v-for="(point, k) in points.filter(e => e.stage === (key + 1))" :key="k"
                    >
                      <span
                        class="
                          text-right
                          font-weight-bold
                          subtitle-2
                          mr-4
                        "
                        style="width: 3ch"
                      >
                        {{ point.amount }}
                      </span>
                      <img
                        @dragstart="e => e.preventDefault()"
                        class="mr-2"
                        color="primary"
                        :src="getErrorImage(point)"
                        width="24px"
                        height="24px"
                      />
                      <p class="
                        d-inline-block
                        my-auto
                        caption
                      ">
                        {{ point.error_type ? point.error_type.name : '' }}
                        {{ point.inclusion_type ? `(${point.inclusion_type.name})` : '' }}
                      </p>
                    </v-flex>
                  </v-layout>
                </v-container>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
          <v-divider class="mt-6 mb-2"></v-divider>
          <v-layout row wrap>
            <v-flex class="d-flex pa-4">
              <span class="subtitle-1 font-weight-bold">
                {{ $t('report.summary.template_preview') }}
              </span>
              <v-spacer></v-spacer>
              <tooltip-left
                icon="mdi-rotate-3d-variant"
                :text= "$t('report.summary.template_toggle')"
                @click="templateInside = !templateInside"
              >
              </tooltip-left>
            </v-flex>
          </v-layout>
          <v-img
            v-if="templateInside"
            :src="`${blueprints ? blueprints.blueprint_inside : ''}?r=${(new Date()).getTime()}`"
          ></v-img>
          <v-img
            v-if="!templateInside"
            :src="`${blueprints ? blueprints.blueprint_outside : ''}?r=${(new Date()).getTime()}`"
          ></v-img>
        </v-card-text>
      </v-flex>
      <v-flex shrink>
        <custom-divider></custom-divider>
      </v-flex>
      <v-flex shrink>
        <v-card-actions class="pa-2">
          <v-btn
            v-if="parent === 'create' && stage > 1"
            small
            text
            @click="updateStep(stage - 1)"
          >
            {{ $t('report.summary.buttons.go_back_button') }}
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn
            v-if="parent === 'create' && stage <= 5"
            small
            color="primary"
            @click="sendReport"
          >
            {{ $t('report.summary.buttons.send_button') }}
          </v-btn>
        </v-card-actions>
      </v-flex>
    </v-card>
  </v-layout>
</template>
<script>
import { mapActions, mapState } from 'vuex'
import CustomDivider from '@/components/reusable/CustomDivider'
import { MAIN_STEPS, BASE_URL } from '@/constants'
import ReportIconTextEntry from './ReportIconTextEntry'
import TooltipLeft from '@/components/reusable/TooltipLeft'

export default {
  name: 'ReportSummary',
  components: {
    ReportIconTextEntry,
    CustomDivider,
    TooltipLeft
  },
  props: {
    parent: String,
    refetch: Boolean
  },
  data () {
    return {
      opened: 0,
      steps: MAIN_STEPS,
      base_url: BASE_URL,
      templateInside: true
    }
  },
  computed: {
    ...mapState('stepper', {
      stage: state => state.step
    }),
    ...mapState('report/report', {
      report: state => state.report
    }),
    ...mapState('report/blueprint', {
      blueprints: state => state.blueprints
    }),
    ...mapState('summaryPoints', {
      loading: state => state.loading,
      points: state => state.points
    }),
    workerData () {
      if (this.report && this.report.created_by) {
        const firstName = this.report.created_by.first_name
        const lastName = this.report.created_by.last_name
        const workerId = this.report.created_by.worker_id
        return `${firstName} ${lastName} (${workerId})`
      }
      return ''
    }
  },
  methods: {
    ...mapActions('stepper', {
      updateStep: 'updateStep'
    }),
    ...mapActions('summaryPoints', {
      fetchAllSummaryPoints: 'fetchAll'
    }),
    ...mapActions('report/report', {
      update: 'update'
    }),
    ...mapActions('report/blueprint', {
      fetchBlueprints: 'fetchOne'
    }),
    getErrorImage (point) {
      return this.getInclusionTypeMarker(point)
        ? this.getInclusionTypeMarker(point)
        : this.getErrorTypeMarker(point)
          ? this.getErrorTypeMarker(point)
          : null
    },
    getErrorTypeMarker (point) {
      return point.error_type ? this.base_url + point.error_type.marker : null
    },
    getInclusionTypeMarker (point) {
      return point.inclusion_type ? this.base_url + point.inclusion_type.marker : null
    },
    closeAction () {
      this.opened = 0
      this.$emit('closeAction')
    },
    sendReport () {
      this.update(this.report.id)
        .then(_ => {
          this.$router.push('/report/list')
        })
    }
  },
  watch: {
    report: {
      handler (nv) {
        if (nv && nv.id) {
          this.fetchAllSummaryPoints({ report: nv.id })
          this.fetchBlueprints(nv.id)
        }
      },
      immediate: true
    }
  }
}
</script>
