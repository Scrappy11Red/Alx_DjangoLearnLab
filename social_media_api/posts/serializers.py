from .models import Post, Comments
from rest_framework import serializers
from django.contrib.auth import get_user_model

class CommentSerializer(serializers.Serializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comments
        fields = ['id', 'author', 'content', 'created_at', 'updated_at']

class PostSerealizer(serializers.Serializer):
    author = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']
