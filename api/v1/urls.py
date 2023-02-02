from django.urls import path

from .views import PostAPIView

urlpatterns = [
    path('test/', PostAPIView.as_view()),
]
