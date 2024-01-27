from django.db import models

# Create your models here.


class Form(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=50,unique=True)
    gender=models.CharField(max_length=12)
    subjects=models.TextField(max_length=300)
    hobbies=models.TextField(max_length=200)
    
    
    def __str__(self):
        return self.name;
    