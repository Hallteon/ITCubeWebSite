from django.contrib import admin

from users.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'profile_picture', 'xp', 'slug')
    list_display_links = ('id', 'user')
    search_fields = ('user', 'id')
    list_filter = ('user',)


admin.site.register(UserProfile, UserProfileAdmin)