<template>
  <div class="chapter-view">
    <div class="container">
      <ChapterList 
        :chapters="chapters" 
        :current-chapter="currentChapter"
        @select="selectChapter"
      />
      <main class="main-content">
        <LoadingSpinner v-if="loading" />
        
        <div v-else-if="error" class="error-state">
          <i class="fas fa-exclamation-triangle"></i>
          <h3>{{ error }}</h3>
          <button @click="goHome">返回首页</button>
        </div>
        
        <ChapterContent 
          v-else-if="currentChapter" 
          :chapter="currentChapter" 
        />
        
        <div v-else class="empty-state">
          <i class="fas fa-book-open"></i>
          <h3>章节不存在</h3>
          <button @click="goHome">返回目录</button>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useChapterStore } from '@/store/chapterStore'
import ChapterList from '@/components/ChapterList.vue'
import ChapterContent from '@/components/ChapterContent.vue'
import LoadingSpinner from '@/components/LoadingSpinner.vue'

const route = useRoute()
const router = useRouter()
const store = useChapterStore()

const chapters = ref([])
const currentChapter = ref(null)
const loading = ref(false)
const error = ref(null)

onMounted(async () => {
  loading.value = true
  await store.fetchChapters()
  chapters.value = store.chapters
  
  if (route.params.id) {
    await fetchChapter(route.params.id)
  }
  
  loading.value = false
})

watch(() => route.params.id, async (newId) => {
  if (newId) {
    await fetchChapter(newId)
  }
})

const fetchChapter = async (id) => {
  try {
    loading.value = true
    await store.fetchChapter(id)
    currentChapter.value = store.currentChapter
    error.value = store.error
  } finally {
    loading.value = false
  }
}

const selectChapter = (chapter) => {
  router.push({ name: 'chapter', params: { id: chapter.chapter_number } })
}

const goHome = () => {
  router.push({ name: 'home' })
}
</script>

<style scoped>
.chapter-view {
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
}

.error-state,
.empty-state {
  text-align: center;
  padding: 3rem;
  color: #7d5d3b;
}

.error-state i,
.empty-state i {
  font-size: 3rem;
  margin-bottom: 1rem;
  color: var(--primary-color);
}

.error-state h3,
.empty-state h3 {
  font-size: 1.5rem;
  margin-bottom: 1.5rem;
}

button {
  background: var(--primary-color);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 30px;
  cursor: pointer;
  font-size: 1rem;
  transition: all 0.3s ease;
}

button:hover {
  background: #6e1515;
  transform: translateY(-2px);
}

@media (max-width: 992px) {
  .container {
    flex-direction: column;
  }
  
  .main-content {
    height: auto;
  }
}
</style>