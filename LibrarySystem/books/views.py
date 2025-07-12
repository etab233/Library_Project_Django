from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, Notification, LibraryUser
from .serializers import BookSerializer, NotificationSerializer, LibraryUserSerializer
#### 
class BookViewSet(viewsets.ModelViewSet):
    serializer_class=BookSerializer
    queryset = Book.objects.all()
####
class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

####
class LibraryUserViewSet(viewsets.ModelViewSet):
    serializer_class = LibraryUserSerializer
    
    def get_queryset(self):
        user = self.request.user
        if (user.is_superuser):
            return LibraryUser.objects.all()
        
        return LibraryUser.objects.filter(name=user.name)