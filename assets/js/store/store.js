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

      obtainJWT: 'http://127.0.0.1:8000/auth/obtain_token/',
      refreshJWT: 'http://127.0.0.1:8000/auth/refresh_token/',
      baseUrl: 'http://127.0.0.1:8000/'
      // Prod env for API
      // obtainJWT: 'https://madera-dev.herokuapp.com/auth/obtain_token/',
      // refreshJWT: 'https://madera-dev.herokuapp.com/auth/refresh_token/',
      // baseUrl: 'https://madera-dev.herokuapp.com/'
    },
    quoteDate: '',
    quoteProject: '',
    quoteProjectRef: '',
    quoteClient: {},
    quoteModules: {},
    quotePrice: '',
    quoteGamme: '',
  },
  getters: {
    getUser: state => {
      if(state.isAuthenticated === true)
        return state.authUser;
    },
    getQuoteDate: state => {
      return state.quoteDate;
    },
    getQuoteProject: state => {
      return state.quoteProject;
    },
    getQuoteProjectRef: state => {
      return state.quoteProjectRef;
    },
    getQuoteGamme: state => {
      return state.quoteGamme;
    },
    getQuoteClient: state => {
      return state.quoteClient;
    },
    getQuoteModules: state => {
      return state.quoteModules;
    },
    getQuotePrice: state => {
      return state.quotePrice;
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
      localStorage.setItem('token', newToken);
      state.jwt = newToken;
    },
    removeToken(state) {
      localStorage.removeItem('token');
      state.jwt = null;
    },
    setQuoteDate(state, date) {
       Vue.set(state, 'quoteDate', date);
    },
    setQuoteProject(state, project) {
       Vue.set(state, 'quoteProject', project);
    },
    setQuoteProjectRef(state, projectRef) {
       Vue.set(state, 'quoteProjectRef', projectRef);
    },
    setQuoteClient(state, client) {
       Vue.set(state, 'quoteClient', client);
    },
    setQuoteModules(state, modules) {
       Vue.set(state, 'quoteModules', modules);
    },
    setQuotePrice(state, price) {
       Vue.set(state, 'quotePrice', price);
    },
    setQuoteGamme(state, gamme) {
       Vue.set(state, 'quoteGamme', gamme);
    }
  }
})