<script setup>
import { ref } from 'vue'

const searchString = ref('')
const status = ref('')

function searchPlayer() {
  status.value = searchString.value
    ? `Player search for "${searchString.value}" will be connected to the API here.`
    : 'Enter a player name to search.'
}
</script>

<template>
  <main class="player-page">
    <h1>Player</h1>
    <p>This page is ready for the player search and history workflow.</p>

    <form @submit.prevent="searchPlayer">
      <label for="player-search">Player name</label>
      <input id="player-search" v-model="searchString" type="search" />
      <button type="submit">Search</button>
    </form>

    <p v-if="status" role="status">{{ status }}</p>
  </main>
</template>

<style scoped>
.player-page {
  max-width: 48rem;
  margin: 0 auto;
  padding: 2rem;
  color: #fff;
  font-family: "MS Sans Serif", "Courier New", monospace;
}

form {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  align-items: end;
  margin-top: 2rem;
}

label {
  flex-basis: 100%;
}

input,
button {
  box-sizing: border-box;
  min-height: 2.25rem;
  padding: 0.4rem 0.6rem;
  font: inherit;
}

input {
  min-width: 16rem;
}
</style>
