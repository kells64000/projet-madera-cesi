import Vue from 'vue';

import vSelect from 'vue-select';
import VueParticles from 'vue-particles';
import moment from 'moment';
import Affix from 'vue-affix';
import Buefy from 'buefy';
import 'buefy/dist/buefy.css';
require('../saas/app.scss');

Vue.filter('formatDate', function(value) {
  if (value) {
    return moment(String(value)).format('DD/MM/YYYY HH:mm')
  }
});

Vue.component('v-select', vSelect);
Vue.use(VueParticles);
Vue.use(Affix);
Vue.use(Buefy);


import router from './router/router.js';
import store from './store/store.js';

import App from "./components/App.vue"
import Login from "./components/Login.vue";
import Dashboard from "./components/Dashboard.vue";
import CreateQuote from "./components/CreateQuote.vue";
import ViewQuote from "./components/ViewQuote.vue";

Vue.config.devtools = false;
Vue.config.debug = false;
Vue.config.silent = true;

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
