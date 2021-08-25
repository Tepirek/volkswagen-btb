import Vue from 'vue'
import Vuex from 'vuex'

import snackbar from '@/store/notifications/snackbar'
import auth from '@/store/auth/auth'
import bodyType from '@/store/bodyType/bodyType'
import color from '@/store/color/color'
import componentType from '@/store/componentType/componentType'
import errorType from '@/store/errorType/errorType'
import inclusionType from '@/store/inclusionType/inclusionType'
import point from '@/store/point/point'
import summaryPoints from '@/store/point/summaryPoints'
import report from '@/store/report/report'
import blueprint from '@/store/report/blueprint'
import stepper from '@/store/report/stepper'
import toolbar from '@/store/global/toolbar'
import history from '@/store/history/history'
import summary from '@/store/summary/summary'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    notification: {
      namespaced: true,
      modules: {
        snackbar
      }
    },
    auth,
    bodyType,
    color,
    componentType,
    errorType,
    inclusionType,
    point,
    summaryPoints,
    report: {
      namespaced: true,
      modules: {
        report,
        blueprint
      }
    },
    stepper,
    toolbar,
    history: {
      namespaced: true,
      modules: {
        history
      }
    },
    summary: {
      namespaced: true,
      modules: {
        summary
      }
    }
  }
})
