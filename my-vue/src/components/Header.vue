<template>
  <header class="app-header">
    <div class="header-content">
      <router-link to="/" class="logo">
        <i class="fas fa-book-open"></i>
        <h1>红楼梦阅读器</h1>
      </router-link>
      <div class="search-container">
        <input 
          type="text" 
          placeholder="搜索章节..." 
          v-model="searchQuery"
          @keyup.enter="searchChapters"
        >
        <button @click="searchChapters">
          <i class="fas fa-search"></i>
        </button>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref } from 'vue'
import { useChapterStore } from '@/store/chapterStore'

const store = useChapterStore()
const searchQuery = ref('')

const searchChapters = () => {
  // 在实际应用中，这里可以实现搜索功能
  console.log('搜索:', searchQuery.value)
}
</script>

<style scoped>
.app-header {
  background: linear-gradient(to right, var(--primary-color), #6e1515);
  color: #f9e8c9;
  padding: 1rem;
  box-shadow: 0 4px 12px var(--shadow-color);
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-content {
  max-width: 1600px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
}

.logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  text-decoration: none;
  color: inherit;
}

.logo i {
  font-size: 2rem;
  color: var(--secondary-color);
}

.logo h1 {
  font-size: 1.8rem;
  font-weight: 700;
  letter-spacing: 2px;
  text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
}

.search-container {
  display: flex;
  gap: 0.5rem;
  flex: 1;
  max-width: 400px;
}

.search-container input {
  flex: 1;
  padding: 0.75rem 1rem;
  border: none;
  border-radius: 30px;
  background: rgba(249, 232, 201, 0.9);
  font-size: 1rem;
  min-width: 150px;
}

.search-container button {
  background: var(--secondary-color);
  color: var(--primary-color);
  border: none;
  border-radius: 50%;
  width: 45px;
  height: 45px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.search-container button:hover {
  background: #e6c260;
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
  }
  
  .search-container {
    max-width: 100%;
  }
}
</style>