require('../saas/app.scss');

import Vue from 'vue';

import VueParticles from 'vue-particles';
Vue.use(VueParticles);

import Login from "./components/Login.vue";

const app = new Vue({
    el: '#app',
    components: {
        Login
    }
});