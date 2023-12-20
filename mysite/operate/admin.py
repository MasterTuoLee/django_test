from django.contrib import admin
from .models import Collect,Comment
# Register your models here.

@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass