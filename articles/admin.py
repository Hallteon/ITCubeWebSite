from django.contrib import admin

from articles.forms import ArticleAdminForm, AddCommentForm
from articles.models import Category, Article, Tag, Comment


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ('id', 'title', 'create_time', 'cover_image', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'create_time')


class CommentAdmin(admin.ModelAdmin):
    form = AddCommentForm
    list_display = ('author', 'article', 'text', 'create_time')
    list_display_links = ('author', 'article')
    search_fields = ('author', 'article')
    list_filter = ('author',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_display_links = ('id', 'name', 'category')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
