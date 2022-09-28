from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    title = models.TextField()
    description =models.TextField()