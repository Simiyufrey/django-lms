from django import forms
from .models import Course,Program,Student,Academic_year,Semester

class CourseForm(forms.ModelForm):
    class Meta():
        model=Course
        fields=['course_code','course_desc','year',"Sem"]

        labels={
            "course_code":"",
            "course_desc":"",
            'year':"",
            'Sem':""
        }

        widgets={
            "course_code":forms.TextInput(attrs={'class':"form-control m-2","placeholder":"Course Code"}),
            "course_desc":forms.TextInput(attrs={'class':"form-control m-2","placeholder":"Course Name"}),
            "year":forms.Select(choices=Student.GENDER_CHOICES,attrs={'class':"form-select m-2","placeholder":"Academic year"}),
            "Sem":forms.Select(choices=Semester.objects.all(),attrs={'class':"form-select m-2","placeholder":"Semesterr"})
        
        }
class ProgrammeForm(forms.ModelForm):
    class Meta:
        model=Program

        fields=["prog_code","prog_name"]
        labels={
            "prog_code":"Programme Code",
            "prog_name":"Programme Name",
            
        }

        widgets={
            "prog_code":forms.TextInput(attrs={'class':"form-control mt-4"}),
            "prog_name":forms.TextInput(attrs={'class':"form-control mt-4"})
        }
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=["student_no","surname","othernames","email",'gender',"national_id",'phone_number',"image","prog_code"]
        
        labels={"student_no":"Student No","surname":"Surname","othernames":"Othernames",
                "email":"Email",
                'gender':'Gender',
                "national_id":"National ID",
                'phone_number':"Mobile",
                "image":"Image File",
                "prog_code":"Program Code"}
        
        widgets={
            "student_no":forms.TextInput(attrs={"class":"form-control mb-3","placeholder":"Student No:"}),
            "surname":forms.TextInput(attrs={"class":"form-control mb-3","placeholder":"Surname:"}),
            "othernames":forms.TextInput(attrs={"class":"form-control mb-3","placeholder":"Othernames:"},),
            "email":forms.EmailInput(attrs={"class":"form-control mb-3","placeholder":"Email:"}),
            "gender":forms.Select(attrs={'class':'form-select mb-2','placeholder':'Select gender'},choices=Student.GENDER_CHOICES),
            "national_id":forms.NumberInput(attrs={"class":"form-control mb-3","placeholder":"National Id:"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
            'phone_number':forms.NumberInput(attrs={"class":"form-control mb-3","placeholder":"Phone number:"}),
            "prog_code":forms.Select(choices=Program.objects.all(),attrs={"class":"form-select"})
            
        }
