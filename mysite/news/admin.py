from django.contrib import admin
from .models import Category, News
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name", )
    list_filter = ("name", )


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ("title", "content")
    list_filter = ("title", "content")

