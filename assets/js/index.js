require('../saas/app.scss');
import Vue from 'vue';

import Demo from "./components/Demo.vue";

const app = new Vue({
    el: '#app',
    components: {
        Demo
    }
});