<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <!-- RouterView directly injects whatever page route you are looking at -->
  <RouterView />
</template>

<style>
/* Global reset to remove margins so the 90s blue covers the entire screen */
body {
  margin: 0;
  padding: 0;
  background-color: #000080;
}
</style>
