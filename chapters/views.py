from rest_framework import viewsets
from .models import Chapter
from .serializers import ChapterSerializer


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    def get_queryset(self):
        queryset = Chapter.objects.all()
        # 添加章节过滤
        chapter_number = self.request.query_params.get('chapter')
        if chapter_number:
            queryset = queryset.filter(chapter_number=chapter_number)
        return queryset