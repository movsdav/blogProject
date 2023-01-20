from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .models import Post
from .forms import PostForm


class PostListView(ListView):
    template_name = 'blogApp/blog.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'


class PostCreateView(CreateView):
    template_name = 'blogApp/create_post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts')

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blogApp/post.html'
