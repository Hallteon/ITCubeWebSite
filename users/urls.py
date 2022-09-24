from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('settings/user', UserSettings.as_view(), name='user_settings'),
    path('settings/profile', ProfileSettings.as_view(), name='profile_settings'),
    path('logout/', logout_user, name='logout'),
    path('notifications/', ShowNotices.as_view(), name='notifications'),
    path('<slug:profile_slug>/', ShowUserProfile.as_view(), name='profile')
]