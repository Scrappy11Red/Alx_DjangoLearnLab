from bookshelf.models import Book
//Updates book title.
updated_book = Book.objects.filter(title = "1984").update(title = "Nineteen Eighty-Four")
// Prints expected output showing the updated title.
print(updated_book)