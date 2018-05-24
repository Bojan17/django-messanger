from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Post
from . import forms

class IndexView(generic.ListView):
    model = Post
    template_name = "posts/index.html"
    context_object_name = "posts"

class CreatePost(LoginRequiredMixin, generic.CreateView):
        form_class = forms.PostForm
        model = Post

class SinglePost(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
