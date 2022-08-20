from django.urls import path
from .views import *

urlpatterns = [
    path('', ShowArticles.as_view(), name='articles'),
    path('<int:article_id>/', ShowArticle.as_view(), name='article'),
    path('category/<slug:category_slug>/', ShowCategory.as_view(), name='category'),
    path('add_article/', AddArticle.as_view(), name='add_article')
]