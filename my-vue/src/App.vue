<template>
  <div class="app-container">
    <Header />
    <router-view v-slot="{ Component }">
      <transition name="fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
    <footer class="app-footer">
      <p>《红楼梦》数字阅读器 | © {{ new Date().getFullYear() }} 古典文学数字典藏计划</p>
    </footer>
  </div>
</template>

<script setup>
import Header from '@/components/Header.vue'
</script>

<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background-color: var(--bg-color);
  color: var(--text-color);
}

.app-footer {
  padding: 1.5rem;
  text-align: center;
  background: linear-gradient(to right, var(--primary-color), #6e1515);
  color: #f9e8c9;
  font-size: 0.9rem;
  margin-top: auto;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>