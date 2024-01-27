from django.shortcuts import render
from django.http import HttpResponse
from Students.models import Program,Course


def subject(request):
    programs=Program.objects.all()
    form=SubjectForm()

    if request.method =="POST":
        form=SubjectForm(request.POST)
        subject=form.save(commit=False)
        subject.save()
        subjects=Subject.objects.all()
        return render(request,"academia/subjects.html",{'programs':programs,'subjects':subjects,'form':form,'success':True})
   
    subjects=Subject.objects.all()
    return render(request,"academia/subjects.html",{'programs':programs,'subjects':subjects,'form':form})
   