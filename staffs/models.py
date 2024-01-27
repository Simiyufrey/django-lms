from django.db import models

# Create your models here.

class Lecturer(models.Model):
    lecturer_no=models.CharField(unique=True,max_length=12)
    surname=models.CharField(max_length=20)
    othernames=models.CharField(max_length=30)
    phone_number=models.PositiveIntegerField(unique=True)
    email=models.EmailField(max_length=30,null=True,blank=True)
    gender=models.CharField(max_length=10)
    image=models.FileField(upload_to="staffs")
    def __str__(self):
        return f"{self.lecturer_no}  {self.surname}"
    
class Department(models.Model):
    dep_code=models.CharField(max_length=20,unique=True)
    dep_name=models.CharField(max_length=50,unique=True)
    fac=models.ForeignKey(to='Faculty',on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.dep_name
    
class Faculty(models.Model):
    fac_code=models.CharField(max_length=10,unique=True)
    fac_name=models.CharField(max_length=60)
    
    def __str__(self):
        return self.fac_name
    
    
    