from django.contrib import admin

from users.models import UserProfile, Notice


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'profile_picture', 'xp', 'slug')
    list_display_links = ('id', 'user')
    search_fields = ('user', 'id')
    list_filter = ('user',)


class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_to', 'text', 'create_time')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Notice, NoticeAdmin)