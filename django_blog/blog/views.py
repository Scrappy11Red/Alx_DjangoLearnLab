from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegisterForm, PostForm
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# Create your views here.

#User registration view 
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
          user = form.save()
          login(request, user)
          messages.success(request, 'Account created successfully!')
          return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.save()
        return redirect('profile')
    return render(request, 'blog/profile.html', {'user': request.user})



class PostCreateView(CreateView):
    template_name = 'blog/post_create.html'
    model = Post
    success_url = '/'
    fields = ['title', 'content']

class PostListView(ListView):
    template_name = 'blog/post_list.html'
    models = Post
    queryset = Post.objects.all()
    templates_name = 'blog/post_list.html'
    
class PostDetailView(DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'
    

class PostUpdateView(UpdateView):
    template_name = 'blog/post_update.html'
    model = Post
    success_url = '/'
    
class PostDeleteView(DeleteView):
    template_name = 'blog/post_delete.html'
    model = Post
    success_url = '/'

