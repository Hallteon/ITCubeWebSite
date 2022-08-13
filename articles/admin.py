from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from articles.models import Category, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'create_time', 'cover_image', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'create_time')
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(DjangoMpttAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
