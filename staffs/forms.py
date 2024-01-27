from django import forms
from .models import Lecturer,Department,Faculty


class lecturer_form(forms.ModelForm):
    class Meta():
        model=Lecturer
        
        fields=['lecturer_no','surname','othernames','phone_number','email','gender','image']
        
        labels={
            'lecturer_no':"Lecturer No",
            'surname':"Surname",
            'othernames':"Othernames",
            'phone_number':"Mobile",
            "email":"Email",
            "gender":"Gender",
            "image":""
        }
        
        widgets={
            'lecturer_no':forms.TextInput(attrs={"class":"form-control my-2"}),
            'surname':forms.TextInput(attrs={"class":"form-control my-2"}),
            'othernames':forms.TextInput(attrs={"class":"form-control my-2"}),
            'phone_number':forms.NumberInput(attrs={"class":"form-control my-2"}),
            "email":forms.EmailInput(attrs={"class":"form-control my-2"}),
            "gender":forms.RadioSelect(attrs={"class":"form-radio d-flex justify-content-around"},choices=[["Female","Female"],["Male","Male"]]),
            "image":forms.FileInput(attrs={"class":"form-control mt-2"})
        }
class FacultyForm(forms.ModelForm):
    class Meta():
        model=Faculty
        fields=['fac_code','fac_name']
        labels={
            'fac_code':'',
            'fac_name':''
        }
        
        widgets={
            'fac_code':forms.TextInput(attrs={'class':'form-control my-2','placeholder':"faculty code",'id':"fac_code"}),
            'fac_name':forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Faculty Name',"id":"fac_name"})
        }