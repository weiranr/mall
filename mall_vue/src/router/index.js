import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home/index.vue'
import HomeMain from '../views/Home/HomeMain.vue'
import SearchList from '../views/Home/SearchList.vue'
import Category from '../views/Category/index.vue'
import Cart from '../views/Cart/index.vue'
import Me from '../views/Me/index.vue'
import level2r1 from '../views/Category/base/level2/level2r1.vue'
import level2r2 from '../views/Category/base/level2/level2r2.vue'
import level2r3 from '../views/Category/base/level2/level2r3.vue'
import level2r4 from '../views/Category/base/level2/level2r4.vue'
import level2r5 from '../views/Category/base/level2/level2r5.vue'
import level2r6 from '../views/Category/base/level2/level2r6.vue'
import level2r7 from '../views/Category/base/level2/level2r7.vue'
import level2r8 from '../views/Category/base/level2/level2r8.vue'
import level2r9 from '../views/Category/base/level2/level2r9.vue'

const routes = [
  {
    path: '',
    redirect: 'Home'
  },
  {
    path: '/Home',
    name: 'Home',
    component: Home,
    children: [
      { path: '', redirect: '/Home/HomeMain' },
      { path: '/Home/HomeMain', component: HomeMain },
      { path: '/Home/SearchList', component: SearchList }
    ]
  },
  {
    path: '/Category',
    name: 'Category',
    component: Category,
    children: [
      { path: '', redirect: '/Category/level2r1' },
      { path: '/Category/level2r1', component: level2r1 },
      { path: '/Category/level2r2', component: level2r2 },
      { path: '/Category/level2r3', component: level2r3 },
      { path: '/Category/level2r4', component: level2r4 },
      { path: '/Category/level2r5', component: level2r5 },
      { path: '/Category/level2r6', component: level2r6 },
      { path: '/Category/level2r7', component: level2r7 },
      { path: '/Category/level2r8', component: level2r8 },
      { path: '/Category/level2r9', component: level2r9 }
    ]
  },
  {
    path: '/Cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/Me',
    name: 'Me',
    component: Me
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
