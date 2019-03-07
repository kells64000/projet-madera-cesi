require('../saas/app.scss');

import Vue from 'vue';

import vSelect from 'vue-select';

import VueParticles from 'vue-particles';

import moment from 'moment';

Vue.filter('formatDate', function(value) {
  if (value) {
    return moment(String(value)).format('DD/MM/YYYY HH:mm')
  }
});

Vue.component('v-select', vSelect);
Vue.use(VueParticles);

import FlashMessage from '@smartweb/vue-flash-message';
Vue.use(FlashMessage);


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
