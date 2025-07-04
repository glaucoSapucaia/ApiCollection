<template>
  <div>
    <h1>Notas</h1>
    <ul>
      <li v-for="nota in notas" :key="nota.id">
        <strong>{{ nota.title }}</strong>: {{ nota.content }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'

const notas = ref([])

onMounted(async () => {
  const res = await fetch('http://localhost:8000/notes/')
  notas.value = await res.json()
})
</script>
