<template>
  <div class="container mx-auto px-4 py-6">
    <h1 class="text-3xl font-bold mb-6">Movies</h1>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="movie in movies" :key="movie.id" class="border rounded-lg shadow-sm p-4 flex">
        <img :src="movie.poster" alt="Movie Poster" class="w-24 h-auto mr-4 object-cover" />
        <div>
          <h2 class="text-xl font-semibold">{{ movie.title }}</h2>
          <p class="text-gray-700">{{ movie.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

let movies = ref([]);

const fetchMovies = async () => {
  try {
    const response = await fetch('/api/v1/movies');
    const data = await response.json();
    movies.value = data.movies;
  } catch (error) {
    console.error('Error fetching movies:', error);
  }
};

onMounted(fetchMovies);
</script>