from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment

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



class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'blog/post_create.html'
    model = Post
    success_url = '/'
    fields = ['title', 'content']

class PostListView(LoginRequiredMixin, ListView):
    template_name = 'blog/post_list.html'
    models = Post
    queryset = Post.objects.all()
    templates_name = 'blog/post_list.html'
    
class PostDetailView(LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'
    

class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'blog/post_update.html'
    model = Post
    success_url = '/'
    
class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'blog/post_delete.html'
    model = Post
    success_url = '/'


#Comment CRUD Section
class CommentCreateView(CreateView, LoginRequiredMixin):
    model = Comment
    template_name = 'blog/comment_form.html'
    fields = ['content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs('pk')
        return super().form_valid(form)
    
class CommentUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    template_name = 'blog/comment_form.html'
    fields = ['content']

class CommentDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    template_name = 'blog/comment_form.html'