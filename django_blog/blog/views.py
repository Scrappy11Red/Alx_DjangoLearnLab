from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, PostForm

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

def update_user_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
        else:
            form = UserUpdateForm(instance=request.user)
        return render(request, 'blog/update.html', {'form': form})
    

def user_login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        redirect("/")
    else:
        # Return an 'invalid login' error message.
        ...