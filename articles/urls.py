from django.urls import path
from .views import *

urlpatterns = [
    path('', ShowArticles.as_view(), name='articles'),
    path('<int:article_id>/', ShowArticle.as_view(), name='article'),
    path('category/<slug:category_slug>/', ShowCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', ShowTag.as_view(), name='tag'),
    path('add_article/', AddArticle.as_view(), name='add_article'),
    path('comments/delete_comment/<int:comment_id>/', DeleteComment.as_view(), name='del_comment'),
]