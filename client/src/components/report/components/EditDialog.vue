<template>
  <div class="text-center">
    <v-dialog v-model="display">
      <v-card>
        <v-card-title class="text-h5 grey lighten-2 mb-3">
          {{ $t('report.edit_dialog.title') }}
        </v-card-title>

        <v-select
          class="mx-4"
          color="primary"
          v-model="errorType"
          :items="errorTypes"
          filled
          :label= "$t('report.edit_dialog.labels.error_type')"
          outlined
        ></v-select>

        <v-select
          v-if="showInclusionTypes"
          class="mx-4"
          color="primary"
          v-model="inclusionType"
          :items="inclusionTypes"
          filled
          :label= "$t('report.edit_dialog.labels.inclusion_type')"
          outlined
        ></v-select>

        <div class="text-center">
          <v-btn color="primary" class="my-4" @click="hideDialog">
            {{ '$t(report.edit_dialog.buttons.apply_buton)' }}
          </v-btn>
        </div>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  name: 'EditDialog',
  data () {
    return {
      errorTypes: [
        'wtracenia',
        'smugi',
        'czarny klej',
        'czerwony klej',
        'wyplywki',
        'kraterki DLK',
        'smugi z KTL',
        'kratery',
        'zacieki',
        'przegazy',
        'peknieta spoina PVC',
        'niedomalowanie',
        'zgorzelina',
        'pyl szlifierski',
        'piasek',
        'zabrSpawalnicze',
        'Film_PVC',
        'Zabrudzenie PVC',
        'Przetrysk_PVC'
      ],
      inclusionTypes: [
        'koagulat',
        'perla',
        'metal',
        'czarny klej',
        'czastka KTL',
        'czastki brazowe',
        'Cu',
        'fosforany',
        'czastki czarne',
        'czastki szare',
        'metal',
        'czastki brazowe',
        'czarne+metal',
        'szare+metal',
        'czastki FL',
        'pod FL',
        'wlokno',
        'klej',
        'PVC',
        'wlokno niebieski',
        'czastki BC',
        'zelka',
        'multikolor',
        'pregi',
        'Zabrudzenie PVC'
      ]
    }
  },
  computed: {
    errorType: {
      ...mapState('editDialog', {
        get: state => state.errorType
      }),
      set (value) {
        this.setErrorType(value)
      }
    },
    inclusionType: {
      ...mapState('editDialog', {
        get: state => state.inclusionType
      }),
      set (value) {
        this.setInclusionType(value)
      }
    },
    display: {
      ...mapState('editDialog', {
        get: (state) => state.display
      }),
      set () {
        this.toggleErrorDialog()
      }
    },
    showInclusionTypes () {
      return this.errorType.localeCompare('wtracenia') === 0
    }
  },
  methods: {
    ...mapActions('editDialog', {
      toggleErrorDialog: 'toggleDisplayVisible',
      setErrorType: 'setErrorTypeValue',
      setInclusionType: 'setInclusionTypeValue'
    }),
    hideDialog () {
      this.display = false
    }
  },
  props: {}
}
</script>

<style>
</style>
