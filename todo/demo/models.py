from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
    
class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=40)
    info = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    
    def __str__(self):
        return self.task
