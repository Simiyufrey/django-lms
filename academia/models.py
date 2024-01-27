from django.db import models

# Create your models here.
class Lecture(models.Model):
    class_code=models.ForeignKey(to="ClassR",on_delete=models.SET_NULL,null=True)
    course=models.ForeignKey(to="Students.Course",on_delete=models.SET_NULL,null=True,blank=True)
    lecturer=models.ForeignKey(to="staffs.Lecturer",on_delete=models.SET_NULL,null=True,blank=True)
    description=models.TextField(max_length=1000)
    date_created=models.DateTimeField(auto_now=True,null=True)
    updated_at=models.DateTimeField(auto_created=True,auto_now_add=True,null=True)

class ClassR(models.Model):
    class_description=models.TextField()
    program=models.ForeignKey(to="Students.Program",on_delete=models.SET_NULL,null=True,blank=True)
    year=models.IntegerField(null=False,blank=False)


class Enrollment(models.Model):
    student=models.ForeignKey(to="Students.Student",on_delete=models.SET_NULL,null=True,blank=True)
    course=models.ForeignKey(to="Students.Course",on_delete=models.SET_NULL,null=True,blank=True)
    