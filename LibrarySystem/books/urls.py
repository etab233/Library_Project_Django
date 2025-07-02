from django.urls import path, include
from rest_framework.routes import DefaultRouter
from .views import BookViewSet

router =DefaultRouter()
router.register(r'books',BookViewSet)

urlpatterns=[
    path('', include(router.urls)),
]