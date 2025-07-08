import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AboutView from '@/views/AboutView.vue'
import NotesView from '@/views/NotesView.vue'
import AddNoteView from '@/views/AddNoteView.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/about', component: AboutView },
  { path: '/notes', component: NotesView },
  { path: '/add-note', component: AddNoteView },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
