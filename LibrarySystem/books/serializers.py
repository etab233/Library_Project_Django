from rest_framework import serializers
from .models import Book, Notification, LibraryUser

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields = '__all__'
        read_only_fields = ['book_id']
        
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields=['notification_id']

class LibraryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryUser
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'borrowed_books', 'notifications']