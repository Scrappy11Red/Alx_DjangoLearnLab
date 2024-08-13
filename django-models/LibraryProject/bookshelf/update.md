from bookshelf.models import Book
//Updates book title.
book = Book.objects.get(title = "1984")
book.title = "Nineteen Eighty-Four"
book.save()
// Prints expected output showing the updated title.
print(retrieve_book)