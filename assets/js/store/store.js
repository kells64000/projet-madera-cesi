import Vue from 'vue';
import VueAxios from 'vue-axios'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex);
Vue.use(VueAxios, axios);

// Make Axios play nice with Django CSRF
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default new Vuex.Store({
  state: {
    authUser: {},
    isAuthenticated: false,
    jwt: localStorage.getItem('token'),
    endpoints: {
      // TODO: Remove hardcoding of dev endpoints
      obtainJWT: 'http://127.0.0.1:8000/auth/obtain_token/',
      refreshJWT: 'http://127.0.0.1:8000/auth/refresh_token/',
      baseUrl: 'http://127.0.0.1:8000/'
    },
    quoteClient: {},
    quoteProject: '',
    quoteModules: {}
  },
  getters: {
    getUser: state => {
      if(state.isAuthenticated === true)
        return state.authUser;
    },
    getQuoteClient: state => {
      return state.quoteClient;
    },
    getQuoteProject: state => {
      return state.quoteProject;
    },
    getQuoteModules: state => {
      return state.quoteModules;
    }
  },
  mutations: {
    setAuthUser(state, {
      authUser,
      isAuthenticated
    }) {
      Vue.set(state, 'authUser', authUser);
      Vue.set(state, 'isAuthenticated', isAuthenticated)
    },
    updateToken(state, newToken) {
      // TODO: For security purposes, take localStorage out of the project.
      localStorage.setItem('token', newToken);
      state.jwt = newToken;
    },
    removeToken(state) {
      // TODO: For security purposes, take localStorage out of the project.
      localStorage.removeItem('token');
      state.jwt = null;
    },
    setQuoteClient(state, client) {
       Vue.set(state, 'quoteClient', client);
    },
    setQuoteProject(state, project) {
       Vue.set(state, 'quoteProject', project);
    },
    setQuoteModules(state, modules) {
       Vue.set(state, 'quoteModules', modules);
    }
  }
})