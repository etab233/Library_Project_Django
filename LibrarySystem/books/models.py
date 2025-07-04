from django.db import models
#كود يعبر عن صف الكتاب 
class Book (models.Model):
    book_id= models.CharField(max_length=10)
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    genre=models.CharField(max_length=50)
    publication_year=models.DateField()
    isAvailable=models.BooleanField(default=False)
    rental_fee=models.FloatField(default=0.0)
    
    def __str__(self):
        return self.title

# كود يعبر عن صف الاشعارات
class Notification(models.Model):
    notification_id= models.CharField(max_length=10)
    message = models.TextField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    notification_type=models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title