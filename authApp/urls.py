from django.urls import path, include

from .views import UserLoginView, UserRegistrationView, ProfileRegistrationView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile_register/', ProfileRegistrationView.as_view(), name='profile_register'),
    path('', include('django.contrib.auth.urls')),
]
