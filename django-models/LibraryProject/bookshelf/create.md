from bookshelf.models import Book
//Creates a Book instance.
book1 = Book.objects.create(title = "1984", author = "George Orwell", publication_year = "1949")
book1.save()
//Prints expected output noting the successful creation.
print(Book.objects.values())