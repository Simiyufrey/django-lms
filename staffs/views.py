from django.shortcuts import render
from .models import Lecturer,Faculty
from .forms import lecturer_form,FacultyForm
from school_ms.file_handler import delete_file
from django.http import JsonResponse

# Create your views here.


def staffs(request):
    if request.method == "POST":
        form=lecturer_form(request.POST,request.FILES)
        if form.is_valid():
            lec=form.save(commit=False)
           
            lec.save()
            
            return render(request,"staffs/staffs.html",{"form":form,"success":True,"message":"Saved successfully"})
    
    lecturers=Lecturer.objects.all()
    return render(request, "staffs/staffs.html",{"form":lecturer_form(),"lecturer":lecturers})

def edit_staff(request,id):
    if request.method == "POST":
        lecturer=Lecturer.objects.get(pk=id)
        form=lecturer_form(request.POST,request.FILES,instance=lecturer)
        delete_file(request,lecturer.image.url)
        lec=form.save(commit=False)
        lec.save()
        return render(request, "staffs/staffs.html",{"lec":form})
    lecturer=Lecturer.objects.get(pk=id)
    form=lecturer_form(instance=lecturer)
    return render(request, "staffs/edit_staff.html",{"form":form})
def view_faculty(request):
    form=FacultyForm()
    faculties=Faculty.objects.all()
    if request.method =="POST":
        form=FacultyForm(request.POST)
        if form.is_valid():
            fac=form.save(commit=False)
            print(fac)
            print(form)
            fac.save()
            faculties=Faculty.objects.all()
            return render(request,'staffs/faculties.html',{'form':form,"faculties":faculties,"success":True,"message":"Saved succeffully"})
        else:
            print(form)
            return render(request,'staffs/faculties.html',{'form':form,"faculties":faculties,"success":True,"message":""})
        
    form=FacultyForm()
    return render(request,'staffs/faculties.html',{'form':form,"faculties":faculties})
     