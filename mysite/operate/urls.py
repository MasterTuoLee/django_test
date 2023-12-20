from django.urls import path
from .views import collect,comment

app_name = "operate"
urlpatterns = [
    path('collect/', collect, name="collect"),
    path('comment/', comment, name="comment"),

]
