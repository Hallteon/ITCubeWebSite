from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from itcube import settings
from main.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('main.urls')),
    path('users/', include('users.urls')),
    path('articles/', include('articles.urls')),
    path('projects/', include('projects.urls')),
    path('categories/', include('categories.urls')),
    path('tags/', include('tags.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found