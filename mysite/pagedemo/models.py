from django.db import models


# Create your models here.
class NewsItem(models.Model):
    title = models.CharField(max_length=8, verbose_name="标题")
    time = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    viewcount = models.PositiveIntegerField(default=0, verbose_name="阅读量")

    def __str__(self):
        return self.title
