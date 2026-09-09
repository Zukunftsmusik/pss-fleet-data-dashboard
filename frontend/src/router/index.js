import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PlayerView from '../views/PlayerView.vue'

const router = createRouter({
  // import.meta.env.BASE_URL automatically reads the 'base' value from vite.config.js
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/player',
      name: 'player',
      component: PlayerView,
    },
  ],
})

export default router
