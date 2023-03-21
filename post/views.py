from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from .models import Post
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView


# from django.views.generic import DetailView


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'


def hello(request):
    posts = Post.Objects.all()
    context = {'post': posts}
    return render(request, 'post/hello.html', {'posts': posts})


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'



class PostCreateView(CreateView):
    model = Post
    template_name = 'post/post_new.html'
    fields = ['title', 'body', 'author']
    success_url = reverse_lazy('home')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('home')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post/post_edit.html'
    fields = ['title', 'body']


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/post_detail.html', {'post': post})


def greet(request):
    return HttpResponse("Welcome to Django, Adeyemi")


def game(request):
    return HttpResponse("I love playing table tennis")
