# your_app_name/urls.py
from django.urls import path
from .views import VideoListCreateView

urlpatterns = [
    path('api/youtube/', VideoListCreateView.as_view(), name='video-list-create'),
]
