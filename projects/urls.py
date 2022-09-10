from django.urls import path
from .views import *

urlpatterns = [
    path('', ShowProjects.as_view(), name='projects')
]