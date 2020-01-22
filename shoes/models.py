from django.db import models
from django.contrib.auth.models import User 

class Shoes(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    brand = models.CharField(max_length=100)
    style = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand

