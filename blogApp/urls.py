from django.urls import path

from .views import PostListView, PostCreateView, PostDetailView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post'),
    path('posts/add/', PostCreateView.as_view(), name='post_add'),
]
