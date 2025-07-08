<script setup>
import { ref, onMounted, computed } from 'vue'

const notes = ref([])
const page = ref(1)
const perPage = 5

const fetchNotes = async () => {
  try {
    const res = await fetch(`http://localhost:8000/notes`)
    notes.value = await res.json()
  } catch (e) {
    console.error(e)
  }
}

onMounted(fetchNotes)

const pagedNotes = computed(() => {
  const start = (page.value - 1) * perPage
  return notes.value.slice(start, start + perPage)
})

const totalPages = computed(() => Math.ceil(notes.value.length / perPage))

const prevPage = () => {
  if (page.value > 1) page.value--
}
const nextPage = () => {
  if (page.value < totalPages.value) page.value++
}
</script>

<template>
  <div class="max-w-4xl mx-auto bg-white text-black p-6 rounded-lg shadow-md">
    <h1 class="text-3xl font-bold mb-6">Notas</h1>

    <div class="grid gap-4 mb-6 sm:grid-cols-1 md:grid-cols-2">
      <div
        v-for="note in pagedNotes"
        :key="note.id"
        class="p-4 border border-gray-700 rounded shadow-sm hover:shadow-md transition bg-gray-50"
      >
        <h2 class="text-xl font-semibold mb-2 text-black">{{ note.title }}</h2>
        <p class="text-gray-800 mb-2">{{ note.content }}</p>
        <p class="text-sm italic text-gray-600 mb-1">Autor: {{ note.author }}</p>
        <p class="text-xs text-gray-500">
          Criado em: {{ new Date(note.created_at).toLocaleDateString() }}
        </p>
      </div>
    </div>

    <div class="flex justify-center space-x-4">
      <button
        @click="prevPage"
        :disabled="page === 1"
        class="px-4 py-2 rounded bg-gray-700 text-white disabled:opacity-50 hover:bg-black transition"
      >
        Anterior
      </button>
      <span class="self-center text-black">Página {{ page }} de {{ totalPages }}</span>
      <button
        @click="nextPage"
        :disabled="page === totalPages"
        class="px-4 py-2 rounded bg-gray-700 text-white disabled:opacity-50 hover:bg-black transition"
      >
        Próximo
      </button>
    </div>
  </div>
</template>
