import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)

// articles를 movielist로 수정..

const API_URL = 'http://127.0.0.1:8000'


export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    articles: [],
    movies : [],
    logedin_user: null,
    user_info: null,
    user_detail: null,
    token: null,
    //isLoggedIn : store.state.token, 
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    // 회원가입 && 로그인
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'home' })
    },
    GET_LOGIN_USER(state, logedin_user) {
      state.logedin_user = logedin_user
      state.user_info = logedin_user
    },
    LOG_OUT(state) {
      //state.recommend_movies = null
      state.logedin_user = null
      state.token = null

      localStorage.removeItem('logedin_user')
      localStorage.removeItem('token')

      //router.push('/')
    },
    GET_USER_INFO(state, user_detail) {
      state.user_detail = user_detail
    },
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          // console.log(res, context)
          console.log(res.data)
          context.commit('GET_MOVIES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getReview(context) {
      axios({
        method : 'get',
        url: `${API_URL}/api/v1/articles/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then(res =>
          context.commit('GET_REVIEWS', res.data)
        )
        .catch(err => console.log(err))
    },
    // signUp(context, payload) {
    //   axios({
    //     method: 'post',
    //     url: `${API_URL}/accounts/signup/`,
    //     data: {
    //       username: payload.username,
    //       password1: payload.password1,
    //       password2: payload.password2,
    //     }
    //   })
    //     .then((res) => {
    //       // console.log(res)
    //       context.commit('SAVE_TOKEN', res.data.key)
    //     })
    // },
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2
        }
      })
      .then((response) => {
        context.commit('SAVE_TOKEN', response.data.key)
        axios({
          method: 'get',
          url: `${API_URL}/accounts/user/`,
          headers: {
            Authorization: `Token ${response.data.key}`
          },
        })
        .then((response) => {
          context.commit('GET_LOGIN_USER', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
      })
      .catch((error) => {
        console.log(error)
      })
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
      .then((response) => {
        context.commit('SAVE_TOKEN', response.data.key)
        axios({
          method: 'get',
          url: `${API_URL}/accounts/user/`,
          headers: {
            Authorization: `Token ${response.data.key}`
          },
        })
        .then((response) => {
          context.commit('GET_LOGIN_USER', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
      })
      .catch((error) => {
        console.log(error)
        window.alert('아이디와 비밀번호를 확인해주세요.')
      })
    },
    getLoginUser(context) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
      })
      .then((response) => {
        context.commit('GET_LOGIN_USER', response.data)
      })
      .catch((error) => {
        console.log(error)
      })
    },
    getUserInfo(context, user_pk){
      axios({
        method: 'get',
        url: `${API_URL}/accounts_detail/${user_pk}`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
      })
      .then((response) => {
        context.commit('GET_USER_INFO', response.data)
      })
      .catch((error) => {
        console.log(error)
      })
    },
  },
  modules: {
    },
  })
