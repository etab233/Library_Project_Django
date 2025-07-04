from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer, NotificationSerializer
#### 
class BookViewSet(viewsets.ModelViewSet):
    serializer_class=BookSerializer
    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
####
class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)