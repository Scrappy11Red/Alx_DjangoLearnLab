from django.shortcuts import render
from typing import Any
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import *
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

def list_books(request):
    books = Book.objects.all()

    return render(request, 'relationship_app/list_books.html', {'book':books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.book_set.all()
        return context
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else: 
            return render(request, 'login.html', {'error': 'Invalid credentials.'})
    else: 
        return render(request, 'login.html')
    
def LogoutView(request):
    logout(request)
    return redirect('login')