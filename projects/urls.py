from django.urls import path
from .views import *

urlpatterns = [
    path('', ShowProjects.as_view(), name='projects'),
    path('<slug:project_slug>/', ShowProject.as_view(), name='project'),
    path('add_project/', AddProject.as_view(), name='add_project'),
    path('category/<slug:category_slug>/', ShowCategoryProjects.as_view(), name='category_projects'),
    path('tag/<slug:tag_slug>/', ShowTagProjects.as_view(), name='tag_projects'),
]