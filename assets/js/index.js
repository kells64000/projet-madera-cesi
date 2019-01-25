require('../saas/app.scss');

import Vue from 'vue';

import VueParticles from 'vue-particles';

Vue.use(VueParticles);

import router from './router/router.js';
import store from './store/store.js';

import Login from "./components/Login.vue";
import Dashboard from "./components/Dashboard.vue";

const app = new Vue({
    el: '#app',
    router,
    store,
    components: {
        Login,
        Dashboard
    }
});