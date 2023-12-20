from django.contrib import admin
from .models import CustomUser,TelephoneCode
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(TelephoneCode)
class TelephoneCodeAdmin(admin.ModelAdmin):
    pass
