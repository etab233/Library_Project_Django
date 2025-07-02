from django.db import models

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
