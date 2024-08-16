# Starts the Python Shell.
py manage.py shell
# Imports The models created in relationship_app/models.py.
from relationship_app.models import Author, Library, Book, Librarian
# Creates 2 authors.
author_1 = Author.objects.create(name = "J. K. Rowling")
author_2 = Author.objects.create(name = "Charles Dickens")
# Saves authors to the database.
author_1.save()
author_2.save()
# Creates 6 books.
book_1 = Book.objects.create(name="Harry Potter And The Philosopher's Stone", author = author_1)
book_2 = Book.objects.create(name="Harry Potter And The Chamber Of Secrets", author = author_1)
book_3 = Book.objects.create(name="Harry Potter And The Prisoner Of Azkaban", author = author_1)
book_4 = Book.objects.create(name="A Tale Of The Two Cities", author = author_2)
book_5 = Book.objects.create(name="Oliver Twist", author = author_2)
book_6 = Book.objects.create(name="Great Expectations", author = author_2)
# Saves books to the database.
book_1.save()
book_2.save()
book_3.save()
book_4.save()
book_5.save()
book_6.save()
# Creates 2 Libraries.
library_1 = Library.objects.create(name = "Library Of Johannesburg")
library_2 = Library.objects.create(name = "Library Of Capt Town")
# Saves libraries to the database.
library_1.save()
library_2.save()
# Adds 3 books to each library.
library_1.books.add(book_1, book_2, book_3)
library_2.books.add(book_4, book_5, book_6)
# Creates 2 Librarians.
librarian_1 = Librarian.objects.create(name = "Bird", library = library_1)
librarian_2 = Librarian.objects.create(name = "Owl", library = library_2)
# Saves librarians to the database
librarian_1.save()
librarian_2.save()

# Query all books by a specific author.
Book.objects.filter(__name__startswith = "J. K.")
# List all books in a library.
Library.objects.values_list("books")
# Retrieve the librarian for a library.
Librarian.objects.values_list("library")