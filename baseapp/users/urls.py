from django.urls import path
from .views import *

app_name = 'users'
urlpatterns = [
    path('adduser/', UserListCreateApiView.as_view(), name="UserListCreateApiView"),
    path('getjobbaseduser/<int:pk>', JobRecommendBasedUserListApiView.as_view(), name="JobRecommendBasedUserListApiView")
]