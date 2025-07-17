<template>
  <div class="home-view">
    <div class="container">
      <ChapterList 
        :chapters="chapters" 
        :current-chapter="currentChapter"
        @select="selectChapter"
      />
      <main class="main-content">
        <div class="empty-state">
          <i class="fas fa-book-open"></i>
          <h3>欢迎阅读《红楼梦》</h3>
          <p>请从左侧选择章节开始阅读</p>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useChapterStore } from '@/store/chapterStore'
import ChapterList from '@/components/ChapterList.vue'

const store = useChapterStore()
const chapters = ref([])
const currentChapter = ref(null)

onMounted(async () => {
  await store.fetchChapters()
  chapters.value = store.chapters
})

const selectChapter = (chapter) => {
  currentChapter.value = chapter
}
</script>

<style scoped>
.home-view {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.container {
  display: flex;
  max-width: 1600px;
  margin: 0 auto;
  flex: 1;
  width: 100%;
}

.main-content {
  flex: 1;
  padding: 2rem;
  overflow-y: auto;
  height: calc(100vh - 80px);
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.empty-state {
  text-align: center;
  padding: 3rem;
  color: #7d5d3b;
  max-width: 500px;
}

.empty-state i {
  font-size: 5rem;
  margin-bottom: 1rem;
  color: var(--border-color);
  opacity: 0.6;
}

.empty-state h3 {
  font-size: 1.8rem;
  margin-bottom: 1rem;
  color: var(--primary-color);
}

.empty-state p {
  font-size: 1.2rem;
}

@media (max-width: 992px) {
  .container {
    flex-direction: column;
  }
  
  .main-content {
    height: auto;
    min-height: 50vh;
  }
}
</style>