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
  <div class="max-w-2xl mx-auto bg-white text-black p-6 rounded-lg shadow-md">
    <h1 class="text-3xl font-bold mb-6">Adicionar Nota</h1>

    <form @submit.prevent="submit" class="space-y-4">
      <div>
        <label class="block mb-1 font-semibold">Título</label>
        <input
          v-model="title"
          type="text"
          required
          class="w-full border border-gray-600 rounded bg-gray-50 px-3 py-2 text-black placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-black"
          placeholder="Digite o título"
        />
      </div>

      <div>
        <label class="block mb-1 font-semibold">Conteúdo</label>
        <textarea
          v-model="content"
          required
          class="w-full border border-gray-600 rounded bg-gray-50 px-3 py-2 text-black placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-black"
          placeholder="Digite o conteúdo"
        ></textarea>
      </div>

      <div>
        <label class="block mb-1 font-semibold">Autor</label>
        <input
          v-model="author"
          type="text"
          required
          class="w-full border border-gray-600 rounded bg-gray-50 px-3 py-2 text-black placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-black"
          placeholder="Nome do autor"
        />
      </div>

      <div>
        <label class="block mb-1 font-semibold">Tags (separadas por vírgula)</label>
        <input
          v-model="tags"
          type="text"
          required
          class="w-full border border-gray-600 rounded bg-gray-50 px-3 py-2 text-black placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-black"
          placeholder="tag1, tag2, tag3"
        />
      </div>

      <div>
        <button
          type="submit"
          class="px-4 py-2 bg-black text-white rounded hover:bg-gray-800 transition"
        >
          Salvar
        </button>
      </div>

      <p v-if="error" class="text-gray-800 mt-2 font-semibold">{{ error }}</p>
      <p v-if="success" class="text-gray-600 mt-2 font-semibold">{{ success }}</p>
    </form>
  </div>
</template>
