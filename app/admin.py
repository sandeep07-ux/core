from .models import Core
from django.contrib import admin


# Register your models here.
@admin.register(Core)
class CoreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}