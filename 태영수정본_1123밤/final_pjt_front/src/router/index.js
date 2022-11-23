import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUpView from '../views/SignUpView.vue'
import LogInView from '../views/LogInView.vue'
import MyPageView from '../views/MyPageView.vue'
import RecommendedView from '../views/RecommendedView.vue'
import LikedMoviesView from '../views/LikedMoviesView.vue'
import UserReviewsView from '../views/UserReviewsView.vue'
import ChangeInfoView from '../views/ChangeInfoView.vue'
import NotFound404 from '../views/NotFound404'
import store from '../store/index.js'
Vue.use(VueRouter)


// router.beforeEach((to, from, next) => {
//   const isLoggedIn = true
//   const authPages = ['recommended', 'mypage']
//   const isAuthRequired = authPages.includes(to.name)
//   if (isAuthRequired && !isLoggedIn) {
//       alert('로그인이 필요한 서비스입니다')
//       next({name: 'login'})
//     } else {
//       next()
//     }
// })
// 이거 고치기 !!
//const isLoggedIn = true
const isLoggedIn = store.state.token
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        alert('이미 로그인 하셨습니다')
        next({name:'home'})
      } else {
        next()
      }
    }
  },
  {
    path: '/login',
    name: 'login',
    component: LogInView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        alert('이미 로그인 하셨습니다')
        next({name:'home'})
      } else {
        next()
      }
    }
  },
  {
    path: '/mypage',
    name: 'mypage',
    component: MyPageView,
    // redirect: "/mypage",
    children: [
      {
        path: 'likedmovies',
        name: 'likedmovies',
        component: LikedMoviesView,
      },
      {
        path: 'userreviews',
        name: 'userreviews',
        component: UserReviewsView,
      },
      {
        path: 'changeinfo',
        name: 'changeinfo',
        component: ChangeInfoView,
      },
    ]
  },
  {
    path: '/recommended',
    name: 'recommended',
    component: RecommendedView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

router.beforeEach((to, from, next) => {
  // 로그인 여부 : 고치기..
  // 2022.11.23 const isLoggedIn = true
  const isLoggedIn = store.state.token

  // 로그인이 필요한 페이지
  const authPages = ['recommended', 'mypage']
  // const allowAllPages = ['login']

  const isAuthRequired = authPages.includes(to.name)
  // const isAuthRequired = !allowAllPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    // console.log('Login으로 이동!')
    alert('로그인이 필요한 페이지입니다')
    next({ name: 'login' })
  } else {
    // console.log('to로 이동!')
    next()
  }
})


