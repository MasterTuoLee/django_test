from django.db import models
from user.models import CustomUser
from news.models import News


# Create your models here.

class OperateBase(models.Model):
    user = models.ForeignKey(CustomUser, models.CASCADE, verbose_name="用户")
    news = models.ForeignKey(News, models.CASCADE, verbose_name="新闻")
    time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        # 存粹抽象类 不能实例化 不会生成数据表
        abstract = True


class Collect(OperateBase):
    class Meta:
        unique_together = [["user", "news"]]

    def __str__(self):
        return f"{self.user.username}  收藏了 {self.news.title}"


class Comment(OperateBase):
    content = models.TextField(verbose_name="评论内容")

    def __str__(self):
        return f"{self.user.username}  评论了 {self.news.title}"
