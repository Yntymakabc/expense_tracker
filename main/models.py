from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
   pass

class Category(models.Model):
    category_name = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"
      
    def __str__(self):
      return self.category_name

