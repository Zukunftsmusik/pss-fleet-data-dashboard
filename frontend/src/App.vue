<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <nav class="site-navigation" aria-label="Main navigation">
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/player">Player</RouterLink>
  </nav>
  <RouterView />
</template>

<style>
/* Global reset to remove margins so the 90s blue covers the entire screen */
body {
  margin: 0;
  padding: 0;
  background-color: #000080;
}

.site-navigation {
  display: flex;
  gap: 1rem;
  padding: 1rem;
  background: #000;
  font-family: "MS Sans Serif", "Courier New", monospace;
}

.site-navigation a {
  color: #00ffff;
}
</style>
