import Vue from 'vue';
import Router from 'vue-router';
import Login from "../components/Login.vue";
import Dashboard from "../components/Dashboard.vue";
import CreateQuote from "../components/CreateQuote.vue";
import ViewQuote from "../components/ViewQuote.vue";

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'Home',
            component: CreateQuote
        },
        {
            path: '/dashboard',
            name: 'Dashboard',
            component: Dashboard
        },
        {
            path: '/quotes/create',
            name: 'CreateQuote',
            component: CreateQuote
        },
        {
            path: '/quotes/view',
            name: 'ViewQuote',
            component: ViewQuote
        }
    ]
})