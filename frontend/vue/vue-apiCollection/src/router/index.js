import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import NotasView from '../views/NotasView.vue'
import NovaNotaView from '../views/NovaNotaView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/notas',
    name: 'notas',
    component: NotasView,
  },
  {
    path: '/nova-nota',
    name: 'nova-nota',
    component: NovaNotaView,
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL), // mais robusto
  routes,
})

export default router
