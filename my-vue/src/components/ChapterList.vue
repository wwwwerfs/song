<template>
  <aside class="sidebar">
    <div class="sidebar-header">
      <h2>章节目录</h2>
      <div class="chapters-count">{{ chapters.length }}回</div>
    </div>
    <div class="chapters-list">
      <div 
        v-for="chapter in chapters" 
        :key="chapter.chapter_number"
        class="chapter-item"
        :class="{ active: isActive(chapter) }"
        @click="selectChapter(chapter)"
      >
        <div class="chapter-number">第{{ chapter.chapter_number }}回</div>
        <div class="chapter-title">{{ chapter.title }}</div>
      </div>
    </div>
  </aside>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue'

const props = defineProps({
  chapters: Array,
  currentChapter: Object
})

const emit = defineEmits(['select'])

const isActive = (chapter) => {
  return props.currentChapter && 
    chapter.chapter_number === props.currentChapter.chapter_number
}

const selectChapter = (chapter) => {
  emit('select', chapter)
}
</script>

<style scoped>
.sidebar {
  width: 320px;
  background: linear-gradient(to bottom, #f5eddd, #f0e4cc);
  border-right: 2px solid var(--border-color);
  overflow-y: auto;
  height: calc(100vh - 80px);
  box-shadow: 3px 0 10px var(--shadow-color);
}

.sidebar-header {
  padding: 1.5rem 1.5rem 1rem;
  border-bottom: 1px solid var(--border-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: sticky;
  top: 0;
  background: inherit;
  z-index: 10;
}

.sidebar-header h2 {
  color: var(--primary-color);
  font-size: 1.4rem;
}

.chapters-count {
  background: var(--primary-color);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.9rem;
}

.chapters-list {
  padding: 0.5rem;
}

.chapter-item {
  padding: 0.9rem 1.2rem;
  margin-bottom: 0.5rem;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  background: rgba(201, 168, 124, 0.1);
  border-left: 3px solid transparent;
}

.chapter-item:hover {
  background: rgba(142, 31, 31, 0.1);
  border-left: 3px solid var(--primary-color);
}

.chapter-item.active {
  background: rgba(142, 31, 31, 0.15);
  border-left: 3px solid var(--primary-color);
  font-weight: 600;
}

.chapter-number {
  width: 36px;
  height: 36px;
  background: var(--primary-color);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 1rem;
  flex-shrink: 0;
  font-size: 0.9rem;
}

.chapter-title {
  flex: 1;
  font-size: 1.05rem;
}

@media (max-width: 992px) {
  .sidebar {
    width: 100%;
    height: auto;
    max-height: 40vh;
    border-right: none;
    border-bottom: 2px solid var(--border-color);
  }
}
</style>