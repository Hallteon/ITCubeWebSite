from django.urls import path
from .views import *

urlpatterns = [
    path('', ShowHomePage.as_view(), name='home'),
]