# In views.py
#Creates a ListView for retrieving all books.

#Applies Django REST Framework’s permission to BookListView class to protect API endpoint based on user roles.

#Creates a DetailView for retrieving a single book by ID.

#Applies Django REST Framework’s permission to BookListDetailView class to protect API endpoint based on user roles.

#Creates a CreateView for adding a new book.

#Applies Django REST Framework’s permission to BookListCreateView classes to protect API endpoint based on user roles.

#Creates an UpdateView for modifying an existing book.

#Applies Django REST Framework’s permission to BookListUpdateView class to protect API endpoint based on user roles.

#Creates a DeleteView for removing a book.

#Applies Django REST Framework’s permission to BookListDeleteView class to protect API endpoint based on user roles.

# In urls.py 
#URL patterns are configure to connect the aforementioned views in views.py with specific endpoints.