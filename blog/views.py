from django.shortcuts import render

# Create your views here.

from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    ordering = '-created_at'