from django.urls import path
from .views import *

urlpatterns = [
    path('articles/<slug:tag_slug>/', ShowTagArticles.as_view(), name='tag_articles'),
    path('projects/<slug:tag_slug>/', ShowTagProjects.as_view(), name='tag_projects'),
]