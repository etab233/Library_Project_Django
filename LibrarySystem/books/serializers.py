from rest_framework import serializers
from .models import Book, Notification

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
        
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'