from django.contrib import admin
from .models import Setting, Request

@admin.register(Setting)
class SettingsCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', "active","navbar_brand","background_image"]
    fields = ['title',"active","navbar_brand","background_image"]

@admin.register(Request)
class RequestCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject']
    readonly_fields = ['name','email','subject','message']