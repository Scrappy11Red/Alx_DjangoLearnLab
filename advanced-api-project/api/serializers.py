from .models import Book, Author
from rest_framework import serializers
from datetime import datetime

#Create a BookSerializer that serializes all fields of the Book model.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    #Add custom validation to the BookSerializer to ensure the publication_year is not in the future.
    def vallidate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

#Create an AuthorSerializer that includes: The name field.
class AuthorSerializer(serializers.ModelSerializer):
    #A nested BookSerializer to serialize the related books dynamically.
    books = BookSerializer.Charfield(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name']