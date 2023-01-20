from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Post
from .forms import PostForm


class PostListView(ListView):
    template_name = 'blogApp/blog.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blogApp/post.html'


class PostCreateView(CreateView):
    template_name = 'blogApp/manipulate_post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts')
    action = 'Create'

    def get_form_kwargs(self, **kwargs):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['action'] = self.action
        return form_kwargs


class PostUpdateView(UpdateView):
    template_name = 'blogApp/manipulate_post.html'
    success_url = reverse_lazy('posts')
    model = Post
    form_class = PostForm
    action = 'Update'

    def get_form_kwargs(self, **kwargs):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['action'] = self.action
        return form_kwargs


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')

    def get(self,req, *args, **kwargs):
        return self.delete(req,*args,**kwargs)
