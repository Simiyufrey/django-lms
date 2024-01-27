from django.db import models

# Create your models here.

class Program(models.Model):
    prog_code=models.CharField(max_length=10,unique=True,primary_key=True)
    prog_name=models.CharField(max_length=50)
    faculty=models.ForeignKey(to="staffs.Faculty", on_delete=models.SET_NULL, max_length=30,null=True,blank=True)
    
    def __str__(self): 
        return f"{self.prog_code}"
    class Meta:
        ordering=['prog_name']
class Student(models.Model):
    GENDER_CHOICES=[("Male","Male"),("Female","Female")]
    student_no=models.CharField(max_length=12,unique=True)
    student_id=models.AutoField(primary_key=True)
    surname=models.CharField(max_length=30)
    othernames=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    date_enrolled=models.DateTimeField(auto_now_add=True)
    gender=models.CharField(max_length=7,choices=GENDER_CHOICES,null=True,blank=True)
    national_id=models.PositiveIntegerField()
    phone_number=models.PositiveIntegerField(unique=True,null=True)
    image=models.FileField(upload_to="uploads",max_length=100)
    year_of_study=models.ForeignKey(to="Year",on_delete=models.SET_NULL,null=True,blank=True)
    prog_code=models.ForeignKey("Program", on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.student_no} {self.surname}"
 
class Academic_year(models.Model):
    CHOICES=[("Active","Active"),("Inactive","Inactive")]
    Academic_year=models.CharField(max_length=10,unique=True)
    status=models.CharField(max_length=10,default='Inactive',choices=CHOICES)
    def __str__(self):
        return self.Academic_year

class Year(models.Model):
    year=models.CharField(max_length=6,unique=True)
    def __str__(self):
        return self.year   
    
class Course(models.Model):
    course_code=models.CharField(primary_key=True,max_length=8)
    course_desc=models.TextField()
    year=models.ForeignKey(to="Year",on_delete=models.CASCADE)
    Sem=models.ForeignKey(to="Semester",on_delete=models.CASCADE)
    prog_code=models.ForeignKey(to="Program",on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.course_code
    
class Sem(models.Model):
    sem=models.CharField(unique=True,max_length=15)
    sem_id=models.AutoField(primary_key=True)
    
    def __str__(self):
        return f"{self.sem}"
class Semester(models.Model):
    sem=models.CharField(unique=True,max_length=15)

    def __str__(self):
        return self.sem
    
class Session1(models.Model):
    academic_year=models.ForeignKey(to="Academic_year",on_delete=models.CASCADE)
    semester=models.ForeignKey(to="Sem",on_delete=models.CASCADE)
    student=models.ForeignKey(to="Student",on_delete=models.SET_NULL,null=True,blank=True)
    
    class Meta:
        unique_together=(("academic_year","semester","student"))
