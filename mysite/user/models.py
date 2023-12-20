from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    telephone = models.CharField(max_length=11, verbose_name="手机号")
    head = models.ImageField(default="head.png", verbose_name="用户头像")
    money = models.PositiveIntegerField(default=0, verbose_name="金币")


class TelephoneCode(models.Model):
    telephone = models.CharField(max_length=11, verbose_name="手机号")
    code = models.CharField(max_length=6, verbose_name="验证码")
    code_type = models.CharField(max_length=20, verbose_name="验证码类型", default="change_telephone_code")