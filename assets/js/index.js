require('../saas/app.scss');

particlesJS.load('particles-js', 'assets/js/plugin/particles.json', function() {});

import Vue from 'vue';

import Login from "./components/Login.vue";

const app = new Vue({
    el: '#app',
    components: {
        Login
    }
});