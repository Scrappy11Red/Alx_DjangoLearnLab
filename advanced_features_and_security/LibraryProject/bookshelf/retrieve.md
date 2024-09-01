from bookshelf.models import Book
//Retrieves book information.
retrieve_book = Book.objects.get(title = "1984", author = "George Orwell", publication_year = "1949").values()
//Prints: expected output showing the details of the book.
print(retrieve_book)