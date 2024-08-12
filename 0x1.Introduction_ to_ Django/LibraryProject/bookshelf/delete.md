from bookshelf.models import Book

book1 = Book.objects.filter(title = "1984", author = "George Orwell", publication_year = "Nineteen Eighty-Four")
//Deletes book
delete_book = book1.delete()
//Prints expected output confirming the deletion.
print(Book.objects.values())
