from django.urls import path
from projects.views import *

urlpatterns = [
    path('', ShowProjects.as_view(), name='projects'),
    path('add_project/', AddProject.as_view(), name='add_project'),
    path('<slug:project_slug>/', ShowProject.as_view(), name='project'),
]