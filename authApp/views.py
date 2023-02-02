from django.contrib.auth import login
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import UserLoginForm, UserRegistrationForm, ProfileSetUpForm
from .models import Profile


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'registration/auth_form.html'
    success_url = reverse_lazy('posts')

    def get(self, request, *args, **kwargs):
        if not isinstance(self.request.user, AnonymousUser):
            return redirect(reverse_lazy('posts'))
        else:
            return super().get(request, *args, **kwargs)


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/auth_form.html'
    model = User
    success_url = reverse_lazy('profile_register')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

    def get(self, request, *args, **kwargs):
        if not isinstance(self.request.user, AnonymousUser):
            return redirect(reverse_lazy('posts'))
        else:
            return super().get(request, *args, **kwargs)


class ProfileRegistrationView(CreateView):
    form_class = ProfileSetUpForm
    template_name = 'registration/auth_form.html'
    model = Profile
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        profile = form.instance
        profile.user = self.request.user
        profile.save()
        return redirect(self.success_url)
