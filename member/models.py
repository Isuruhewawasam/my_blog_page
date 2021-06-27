from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userpro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

