require('../saas/app.scss');

import Vue from 'vue';

import VueParticles from 'vue-particles';
import VueDragResize from 'vue-drag-resize';

Vue.use(VueParticles);
Vue.component('vue-drag-resize', VueDragResize);

import router from './router/router.js';
import store from './store/store.js';

import App from "./components/App.vue"
import Login from "./components/Login.vue";
import Dashboard from "./components/Dashboard.vue";
import CreateQuote from "./components/CreateQuote.vue";
import ViewQuote from "./components/ViewQuote.vue";

new Vue({
    el: '#app',
    render: h => h(App),
    router,
    store,
    template: '<App/>',
    components: {
        App,
        Login,
        Dashboard,
        CreateQuote,
        ViewQuote
    }
});