from django.contrib import admin

from tags.models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_display_links = ('id', 'name', 'category')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Tag, TagAdmin)
