from django.contrib import admin

from notifications.models import Notice, ProjectApplication


class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_to', 'text', 'create_time')


class ProjectApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'project', 'text', 'create_time')


admin.site.register(Notice, NoticeAdmin)
admin.site.register(ProjectApplication, ProjectApplicationAdmin)