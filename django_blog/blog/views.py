from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

#User registration view 
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        user = form.save()
        login(request, user)
        messages.success(request, 'Account created successfully!')
        return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})