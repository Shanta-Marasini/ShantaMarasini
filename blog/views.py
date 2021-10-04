from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post
# Create your views here.

class PostList( ListView ):

    model = Post
    context_object_name = 'posts'



class PostDetail(DetailView):

    model = Post
    context_object_name = 'post'
