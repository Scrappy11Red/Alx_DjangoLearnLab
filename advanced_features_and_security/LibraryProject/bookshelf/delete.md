from bookshelf.models import Book

book = Book.objects.filter(title = "1984", author = "George Orwell", publication_year = "Nineteen Eighty-Four")
//Deletes book
delete_book = book.delete()
//Prints expected output confirming the deletion.
print(Book.objects.values())