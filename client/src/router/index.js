import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'
import Login from '@/components/auth/login/views/LoginView'

import ProfileView from '@/components/profile/view/ProfileView'
import ProfileToolbar from '@/components/toolbar/ProfileToolbar'

import NewReport from '@/components/report/view/NewReport'
import NewReportToolbar from '@/components/toolbar/NewReportToolbar'

import CreateReport from '@/components/report/view/CreateReport'
import CreateReportToolbar from '@/components/toolbar/CreateReportToolbar'

import ListReport from '@/components/report/view/ListReport'
import ListReportToolbar from '@/components/toolbar/ListReportToolbar'

import HistoryView from '@/components/history/view/HistoryView'
import HistoryToolbar from '@/components/toolbar/HistoryToolbar'

import StatisticsToolbar from '@/components/toolbar/StatisticsToolbar'
import StatisticsView from '@/components/statistics/view/StatisticsView'

Vue.use(VueRouter)

const routes = [
  {
    path: '',
    name: 'Login',
    component: Login
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/profile',
    name: 'Profile',
    components: {
      default: ProfileView,
      toolbar: ProfileToolbar
    }
  },
  {
    path: '/report/new',
    name: 'NewReport',
    components: {
      default: NewReport,
      toolbar: NewReportToolbar
    }
  },
  {
    path: '/report/create/:slug',
    name: 'CreateReport',
    components: {
      default: CreateReport,
      toolbar: CreateReportToolbar
    }
  },
  {
    path: '/report/list',
    name: 'ListReport',
    components: {
      default: ListReport,
      toolbar: ListReportToolbar
    }
  },
  {
    path: '/statistics',
    name: 'StatisticsView',
    components: {
      default: StatisticsView,
      toolbar: StatisticsToolbar
    }
  },
  {
    path: '/history',
    name: 'HistoryView',
    components: {
      default: HistoryView,
      toolbar: HistoryToolbar
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.name !== 'Login' && !store.getters['auth/isInit'] && !store.getters['auth/isFetching']) {
    store.dispatch('auth/fetch')
  }

  if (to.name !== 'Login' && !store.getters['auth/isAuthenticated']) {
    return next('/login')
  }

  if (to.name === 'Login' && store.getters['auth/isAuthenticated']) {
    return next('/profile')
  }

  return next()
})

export default router
