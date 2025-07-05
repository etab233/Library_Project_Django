from rest_framework import serializers
from .models import Book, Notification, LibraryUser

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
        
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class LibraryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryUser
        fields = 'all'
        read_only_fields = ['id', 'created_at', 'updated_at', 'borrowed_books', 'notifications']