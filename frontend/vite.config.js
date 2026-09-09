import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [
    vue(),
    {
      name: 'dashboard-base-redirect',
      configureServer(server) {
        server.middlewares.use((request, response, next) => {
          if (request.url === '/dashboard' || request.url?.startsWith('/dashboard?')) {
            response.statusCode = 307
            response.setHeader('Location', '/dashboard/')
            response.end()
            return
          }
          next()
        })
      },
    },
  ],
  base: '/dashboard/', // Match your CapRover subfolder routing
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    proxy: {
      // Forwards local frontend /dashboard/api requests to the Python gateway.
      '/dashboard/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        secure: false,
      }
    }
  }
})
