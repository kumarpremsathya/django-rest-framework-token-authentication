from django.db import models

# Create your models here.
# models.py
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def get_default_user():
    user, _ = get_user_model().objects.get_or_create(username='default_user')
    return user.pk  # Return the primary key value

class Product(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='products', default=get_default_user)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)