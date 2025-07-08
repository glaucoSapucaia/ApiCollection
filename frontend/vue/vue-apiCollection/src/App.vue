<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="flex flex-col min-h-screen">
    <header class="bg-white shadow-md p-4 flex items-center justify-between max-w-7xl mx-auto w-full sticky top-0 z-50">
      <img alt="Logo" class="w-24 h-24" src="@/assets/logo.svg" />
      <nav class="space-x-6 text-lg">
        <RouterLink to="/" class="text-blue-600 hover:underline">Home</RouterLink>
        <RouterLink to="/about" class="text-blue-600 hover:underline">Sobre</RouterLink>
      </nav>
    </header>

    <main class="flex-grow max-w-7xl mx-auto w-full p-6">
      <RouterView />
    </main>

    <footer class="bg-gray-100 text-center py-4 text-sm text-gray-600 max-w-7xl mx-auto w-full mt-auto">
      Direitos reservados - Glauco Sapucaia
    </footer>
  </div>
</template>
