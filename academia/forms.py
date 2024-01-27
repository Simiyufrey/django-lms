from django import forms
from .models import Enrollment



class EnrollmentForm(forms.ModelForm):
    class Meta:
        model=Enrollment

        fields=['student','course']
        labels={
            'student':'Student',
            'course':'Course'
        }
        widgets={
            'student':forms.Select(attrs={'class':'form-select mx-2 my-2'}),
            'course':forms.Select(attrs={'class':'form-control mx-2 my-2'})
        }