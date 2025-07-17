import { defineStore } from 'pinia'
import { ref } from 'vue'
import { getChapters, getChapter } from '@/services/api'

export const useChapterStore = defineStore('chapter', () => {
  const chapters = ref([])
  const currentChapter = ref(null)
  const loading = ref(false)
  const error = ref(null)
  
  const fetchChapters = async () => {
    try {
      loading.value = true
      const data = await getChapters()
      chapters.value = data
      error.value = null
    } catch (err) {
      error.value = '获取章节列表失败，请稍后重试'
      console.error(err)
    } finally {
      loading.value = false
    }
  }
  
  const fetchChapter = async (id) => {
    try {
      loading.value = true
      const data = await getChapter(id)
      currentChapter.value = data
      error.value = null
    } catch (err) {
      error.value = '获取章节内容失败，请稍后重试'
      console.error(err)
    } finally {
      loading.value = false
    }
  }
  
  return {
    chapters,
    currentChapter,
    loading,
    error,
    fetchChapters,
    fetchChapter
  }
})