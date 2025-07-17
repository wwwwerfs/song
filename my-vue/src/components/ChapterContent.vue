<template>
  <div class="chapter-content">
    <div class="chapter-header">
      <h2 class="chapter-title-main">第{{ chapter.chapter_number }}回 {{ chapter.title }}</h2>
      <div class="chapter-subtitle">《红楼梦》经典章节</div>
    </div>
    
    <div class="content" v-html="formattedContent"></div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  chapter: Object
})

const formattedContent = computed(() => {
  if (!props.chapter.content) return ''
  
  // 将内容分割为段落
  const paragraphs = props.chapter.content.split('\n\n')
  
  // 创建带样式的段落
  return paragraphs.map(para => 
    `<p>${para.replace(/\n/g, '<br>')}</p>`
  ).join('')
})
</script>

<style scoped>
.chapter-content {
  max-width: 800px;
  margin: 0 auto;
}

.chapter-header {
  text-align: center;
  margin-bottom: 3rem;
  padding-bottom: 1.5rem;
  border-bottom: 2px solid var(--border-color);
}

.chapter-title-main {
  font-size: 2rem;
  color: var(--primary-color);
  margin-bottom: 0.5rem;
  position: relative;
  display: inline-block;
}

.chapter-title-main:after {
  content: "";
  position: absolute;
  bottom: -10px;
  left: 25%;
  width: 50%;
  height: 3px;
  background: var(--secondary-color);
}

.chapter-subtitle {
  font-size: 1.1rem;
  color: #7d5d3b;
  font-style: italic;
}

.content {
  font-size: 1.15rem;
  line-height: 2;
  text-align: justify;
}

.content >>> p {
  margin-bottom: 1.5rem;
  text-indent: 2em;
}

@media (max-width: 768px) {
  .chapter-header {
    margin-bottom: 2rem;
  }
  
  .chapter-title-main {
    font-size: 1.7rem;
  }
  
  .content {
    font-size: 1.05rem;
    line-height: 1.8;
  }
}
</style>