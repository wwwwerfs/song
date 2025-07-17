from django.db import models

# Create your models here.
class Chapter(models.Model):
    chapter_number = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'chapters'  # 指定数据库表名
        app_label = 'chapters'
        ordering = ['chapter_number']

    def __str__(self):
        return f"第{self.chapter_number}回 {self.title}"