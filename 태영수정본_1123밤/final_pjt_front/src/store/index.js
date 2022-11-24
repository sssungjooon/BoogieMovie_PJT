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
    loginAuthError: null,
    signupAuthError: null,

    //isLoggedIn : store.state.token, 
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
    loginAuthError: state => state.loginAuthError,
    signupAuthError: state => state.signupAuthError,
    authHeader: state => ({ Authorization: `Token ${state.token}`}),
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
    SET_LOGIN_AUTH_ERROR: (state, error) => state.loginAuthError = error,
    SET_SIGNUP_AUTH_ERROR: (state, error) => state.signupAuthError = error,
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
          password2: payload.password2,
          genres: payload.genres
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
          // payload.genres.map(genreId => {
          //   axios({
          //     url: `${API_URL}/movies/`  `url/movies/${TMDBGenreId}/genre/` movies.likeGenre(genreId),
          //     method: 'post',
          //     headers: this.getters.authHeader
          //   })
          // })
        })
        .catch((error) => {
          console.log(error)
          alert('잘못 입력하셨습니다.')
        })
      })
      .catch((error) => {
        console.log(error)
        // if (this.username in  ) {
        //   alert('이미 존재하는 아이디입니다.')
        // }
        if (this.password1 != this.password2) {
          alert(`잘못 입력하셨습니다.
  같은 비밀번호를 입력해 주세요.`)
          } else {alert(`잘못 입력하셨습니다.
비밀번호는 8자 이상이어야 합니다.`  )
      }})
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
