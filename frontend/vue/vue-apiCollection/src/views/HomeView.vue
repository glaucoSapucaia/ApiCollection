<template>
  <div class="max-w-4xl mx-auto">
    <h1 class="text-3xl font-bold mb-6">Bem-vindo ao APICollection</h1>
    <nav class="space-x-4 mb-8">
      <router-link
        to="/notes"
        class="text-blue-600 hover:underline"
      >Ver Notas</router-link>
      <router-link
        to="/add-note"
        class="text-blue-600 hover:underline"
      >Adicionar Nota</router-link>
    </nav>
    <p class="text-gray-700">Use o menu acima para gerenciar suas notas.</p>
  </div>
</template>
