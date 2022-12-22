import Vue from 'vue';
import Router from 'vue-router';
import Sales from '../components/Sales.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Sales',
      component: Sales,
    }
  ],
});