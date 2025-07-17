import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000/api/chapters/'

export const getChapters = async () => {
  const response = await axios.get(API_BASE_URL)
  return response.data
}

export const getChapter = async (id) => {
  const response = await axios.get(`${API_BASE_URL}?chapter=${id}`)
  return response.data[0] // 假设API返回数组，取第一个
}