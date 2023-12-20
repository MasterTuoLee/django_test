from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=10, verbose_name="分类名")

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=20, verbose_name="新闻标题")
    content = CKEditor5Field(verbose_name='新闻正文', config_name='extends')
    time = models.DateTimeField(auto_now_add=True, verbose_name="时间")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name="所属分类")

    def __str__(self):
        return self.title
