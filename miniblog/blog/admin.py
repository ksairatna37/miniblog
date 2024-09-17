from django.contrib import admin
from .models import Post,About
# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']
    
@admin.register(About)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ['desc']
