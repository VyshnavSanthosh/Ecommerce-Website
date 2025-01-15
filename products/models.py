from unicodedata import category
from django.db import models

# Create your models here.

class Product(models.Model):
    LIVE = 1
    DELETE = 0
    STATUS = (
        (LIVE, 'Live'),
        (DELETE, 'Delete'),
    )
    title = models.CharField(max_length=100)
    price = models.FloatField(max_length=10)
    ratings = models.IntegerField()
    photo = models.ImageField(upload_to='media/',null=True)
    description = models.TextField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_status = models.IntegerField(choices=STATUS ,default=LIVE)

    def __str__(self):
        return self.title
