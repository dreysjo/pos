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

const cors = require('cors');
const corsOptions ={
    origin:'http://localhost:5000',
    credentials:true,            //access-control-allow-credentials:true
    optionSuccessStatus:200
}
app.use(cors(corsOptions));