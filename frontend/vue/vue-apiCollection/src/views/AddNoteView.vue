<script setup>
import { ref } from 'vue'

const title = ref('')
const content = ref('')
const author = ref('')
const tags = ref('')

const error = ref('')
const success = ref('')

const submit = async () => {
  error.value = ''
  success.value = ''

  if (!title.value || !content.value || !author.value || !tags.value) {
    error.value = 'Todos os campos são obrigatórios.'
    return
  }

  try {
    const res = await fetch('http://localhost:8000/notes/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        title: title.value,
        content: content.value,
        author: author.value,
        tags: tags.value,
      }),
    })

    if (!res.ok) {
      throw new Error('Erro ao salvar a nota.')
    }

    success.value = 'Nota adicionada com sucesso!'
    title.value = ''
    content.value = ''
    author.value = ''
    tags.value = ''
  } catch (e) {
    error.value = e.message
  }
}
</script>

<template>
  <div class="max-w-2xl mx-auto">
    <h1 class="text-3xl font-bold mb-6">Adicionar Nota</h1>

    <form @submit.prevent="submit" class="space-y-4">
      <div>
        <label class="block mb-1 font-semibold">Título</label>
        <input v-model="title" type="text" required
          class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-green-500" />
      </div>

      <div>
        <label class="block mb-1 font-semibold">Conteúdo</label>
        <textarea v-model="content" required
          class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-green-500"></textarea>
      </div>

      <div>
        <label class="block mb-1 font-semibold">Autor</label>
        <input v-model="author" type="text" required
          class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-green-500" />
      </div>

      <div>
        <label class="block mb-1 font-semibold">Tags (separadas por vírgula)</label>
        <input v-model="tags" type="text" required
          class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-green-500" />
      </div>

      <div>
        <button
          type="submit"
          class="px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700"
        >
          Salvar
        </button>
      </div>

      <p v-if="error" class="text-red-600">{{ error }}</p>
      <p v-if="success" class="text-green-600">{{ success }}</p>
    </form>
  </div>
</template>
