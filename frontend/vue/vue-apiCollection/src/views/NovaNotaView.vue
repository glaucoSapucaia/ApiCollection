<template>
  <div>
    <h1>Nova Nota</h1>
    <form @submit.prevent="adicionarNota">
      <input v-model="title" placeholder="Título" required />
      <textarea v-model="content" placeholder="Conteúdo" required></textarea>
      <button type="submit">Salvar</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const title = ref('')
const content = ref('')
const router = useRouter()

const adicionarNota = async () => {
  await fetch('http://localhost:8000/notes/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title: title.value, content: content.value }),
  })

  router.push('/notas')
}
</script>
