from django.urls import path
from .views import *

urlpatterns = [
    path('', ShowArticles.as_view(), name='articles'),
    path('article/<slug:article_slug>/', ShowArticle.as_view(), name='article'),
    path('add_article/', AddArticle.as_view(), name='add_article')
]