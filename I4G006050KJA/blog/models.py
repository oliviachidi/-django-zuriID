from tkinter import CASCADE
from typing import Text
from django.db import models
from time import timezone
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE, default="title")
    Created_date = models.DateField()
    Published_date = models.DateField()
