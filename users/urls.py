from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('settings/', index, name='settings'),
    path('logout/', logout_user, name='logout'),
    path('<slug:profile_slug>/', ShowUserProfile.as_view(), name='profile'),
]