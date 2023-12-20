
from .views import index, detail

from django.urls import path

app_name = "news"
urlpatterns = [
    path('', index, name="index"),
    path('detail/<int:id>', detail, name="detail"),

]
