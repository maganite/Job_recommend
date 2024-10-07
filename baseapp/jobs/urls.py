from django.urls import path
from .views import *

app_name = 'jobs'
urlpatterns = [
    path('job/', JobListCreateApiView.as_view(), name="JobListCreateApiView"),
    path('getjob/', JobRecommendListApiView.as_view(), name="JobRecommendListApiView")
]