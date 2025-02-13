from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    documentNumber = models.CharField(max_length=14, unique=True)
    documentType = models.CharField(max_length=2)
    cellPhone = models.CharField(max_length=10)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []