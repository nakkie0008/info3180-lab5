<template>
    <div class="card card-body">
      <!-- Success message -->
      <div v-if="successMessage" class="alert alert-success" role="alert">
        {{ successMessage }}
      </div>
  
      <!-- Error messages -->
      <div v-if="errors.length" class="alert alert-danger" role="alert">
        <ul>
          <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
        </ul>
      </div>
  
      <form id="movieForm" @submit.prevent="saveMovie">
        <div class="mb-3">
          <label for="title" class="form-label">Movie Title</label>
          <input type="text" name="title" class="form-control" placeholder="Enter a title"/>
        </div>
  
        <div class="mb-3">
          <label for="description" class="form-label">Description</label>
          <textarea name="description" class="form-control" rows="3" placeholder="Enter a description"></textarea>
        </div>
  
        <div class="mb-3">
          <label for="poster" class="form-label">Poster</label>
          <input
            type="file"
            name="poster"
            class="form-control"
          />
        </div>
  
        <button type="submit" class="btn btn-primary">
          Submit
        </button>
      </form>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";


const csrf_token = ref("");
const successMessage = ref("");
const errors = ref([]);

function getCsrfToken() {
  fetch("/api/v1/csrf-token")
    .then((response) => response.json())
    .then((data) => {
      csrf_token.value = data.csrf_token;
    })
    .catch((error) => {
      console.log("Error fetching CSRF token:", error);
    });
}

function saveMovie() {
  successMessage.value = "";
  errors.value = [];

  let movieForm = document.getElementById("movieForm");

  let form_data = new FormData(movieForm);

  fetch("/api/v1/movies", {
    method: "POST",
    body: form_data,
    headers: {
      "X-CSRFToken": csrf_token.value,
    },
  })
    .then((response) => {
      return response.json().then((data) => {
        return { status: response.status, body: data };
      });
    })
    .then(({ status, body }) => {
      if (status >= 200 && status < 300) {
        successMessage.value = body.message || "Movie was saved successfully!";
      } else {
        if (body.errors) {
          errors.value = body.errors;
        } else {
          errors.value = [body.message || "An error occurred."];
        }
      }
    })
    .catch((error) => {
      console.log("An error occurred:", error);
      errors.value = ["A network error occurred."];
    });
}
onMounted(() => {
  getCsrfToken();
});
</script>

<style scoped>

.movie-form {
  max-width: 600px;  
  margin: 2rem auto;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}

.alert {
  margin-bottom: 1rem;
}

.btn {
  padding: 0.75rem;
  font-size: 1rem;
}

.form-control {
  margin-bottom: 0.75rem;
}

@media (max-width: 576px) {
  .movie-form {
    margin: 1rem;
    padding: 1rem;
  }
}
</style>