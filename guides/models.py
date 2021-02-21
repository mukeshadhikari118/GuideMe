from django.db import models

# Create your models here.
class guide(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    contact = models.PositiveIntegerField(unique=True)
    address1 = models.TextField()
    address2 = models.TextField()
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=32)
    bio = models.TextField()
    pan = models.TextField()
    pp = models.ImageField()
    citizenship = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

