from django.urls import path
from .views import *

urlpatterns = [
    path('', ShowNotices.as_view(), name='notifications'),
    path('<slug:project_slug>/send_application', SendProjectApplication.as_view(), name='send_project_application'),
    path('confirm_application/<int:application_id>', ConfirmProjectApplication.as_view(), name='confirm_project_application'),
    path('reject_application/<int:application_id>', RejectProjectApplication.as_view(), name='reject_project_application'),
    path('confirm_notice/<int:notice_id>', ConfirmNotice.as_view(), name='confirm_notice')
]