from django.shortcuts import render
from typing import Any

# Create your views here.
from  .models import Library
from django.views.generic import DetailView


def book_list(request):
    books = Book.objects.all()

    return render(request, 'books/list_books.html', {'book':books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/list_books.html", "from .models import Library"
    context_object_name = 'library'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.book_set.all()
        return context