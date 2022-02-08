import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import api from './api/index.js'
import {
Tabbar, TabbarItem, Button, Swipe, SwipeItem, Lazyload, Search, Col, Row, Icon, Grid, GridItem, Image as VanImage,
Sidebar, SidebarItem, Toast
} from 'vant'

const app = createApp(App)
app.config.globalProperties.$api = api
app.use(Tabbar).use(TabbarItem).use(Button).use(Swipe).use(SwipeItem).use(Lazyload).use(Search)
.use(Col).use(Row).use(Icon).use(Grid).use(GridItem).use(VanImage).use(Sidebar).use(SidebarItem)
.use(Toast)

app.use(store).use(router)
app.mount('#app')
