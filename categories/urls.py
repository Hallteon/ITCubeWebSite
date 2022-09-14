from django.urls import path
from .views import *

urlpatterns = [
    path('articles/<slug:category_slug>/', ShowCategoryArticles.as_view(), name='category_articles'),
    path('projects/<slug:category_slug>/', ShowCategoryProjects.as_view(), name='category_projects'),
]