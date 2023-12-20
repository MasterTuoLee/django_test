
from .views import login, regist,logout,center,change_head,active,change_username,change_telephone,modify_telephone

from django.urls import path


app_name = "user"
urlpatterns = [
    path('login/', login, name="login"),
    path('regist/', regist, name="regist"),
    path('active/<str:id>', active, name="active"),

    path('logout/', logout, name="logout"),
    path('center/', center, name="center"),
    path('change_head/', change_head, name="change_head"),
    path('change_username/', change_username, name="change_username"),
    path('change_telephone/', change_telephone, name="change_telephone"),
    path('modify_telephone/', modify_telephone, name="modify_telephone"),

]
