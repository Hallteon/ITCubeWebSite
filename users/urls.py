from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('profile/', index, name='profile'),
    path('settings/', index, name='settings'),
    path('logout/', logout_user, name='logout')
]