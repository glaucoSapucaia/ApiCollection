<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <header class="flex flex-col items-center justify-center p-6 md:flex-row md:justify-between bg-white shadow-md">
    <img alt="Vue logo" class="w-28 h-28" src="@/assets/logo.svg" />

    <div class="flex flex-col items-center md:items-start">
      <HelloWorld msg="You did it!" />

      <nav class="mt-4 space-x-4 text-sm">
        <RouterLink to="/" class="text-blue-600 hover:underline">Home</RouterLink>
        <RouterLink to="/about" class="text-blue-600 hover:underline">About</RouterLink>
      </nav>
    </div>
  </header>

  <main class="p-6">
    <RouterView />
  </main>
</template>