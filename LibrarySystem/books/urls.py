from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, NotificationViewSet

router =DefaultRouter()
router.register(r'books',BookViewSet)
router.register(r'notifications', NotificationViewSet, basename='notification')

urlpatterns=[
    path('', include(router.urls)),
]