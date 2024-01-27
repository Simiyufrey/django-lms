from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .models import Course,Program,Student,Semester,Academic_year,Session1
from staffs.models import Lecturer
from .forms import StudentForm,ProgrammeForm,CourseForm
from django.db.models import Q
from django.core import serializers
from  school_ms.file_handler import delete_file
from django.conf import settings
def index(request):
    details=[]
    d={Course,Student,Program,Lecturer}
    colors=["#ab56de","#ee88de","#cc86ce","#cbc2da"]
    for d1,c in zip(d,colors):
        number=d1.objects.all().count()
        name=d1.__name__
        details.append({"name":name,"count":number,"color":c})
    return render(request, "students/index.html",{"courses":Course.objects.all(),"details":details})

def view_course(request,pro):
    years=Academic_year.objects.all()
    sems=Semester.objects.all()
    if request.method =="POST":
        form=CourseForm(request.POST)
        if form.is_valid():
           course=form.save(commit=False)
           print(request.POST)
           programs=Program.objects.get(prog_code=pro)
           course.prog_code=programs
           course.save()
           courses=Course.objects.filter(prog_code=pro).order_by("Academic_year")
           return render(request,'students/courses.html',{"courses":courses,"form":CourseForm(),"success":True,"years":years,"sems":sems})
    courses=Course.objects.filter(prog_code=pro).order_by("Academic_year")
    form=CourseForm()

    return render(request,'students/courses.html',{"courses":courses,"form":form,"years":years,"sems":sems})

def courses(request):
    
    if request.method == "POST": 
        form=CourseForm(request.POST)
        if form.is_valid():
            print(request.POST)
            course=CourseForm.save()
            course.save()

            return render(request, "students/add.html",{"form":CourseForm(),"success":True})
    else:
        form =CourseForm()
        return render(request, "students/add.html",
        {"form":CourseForm(),
        "content":"Godfrey"})
def edit_course(request,id):
    if request.method == "POST":
        course=Course.objects.get(pk=id)
        form=CourseForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
            return render(request, "students/edit.html",
            {"form":form,"success":True})
    else:
        course=Course.objects.get(pk=id)
        form=CourseForm(instance=course)

        return render(request, "students/edit.html",{
            "form":form
        })
def delete_course(request,id):
    course=Course.objects.get(pk=id)
    course.delete()

    return HttpResponseRedirect(reverse('index'))
def programs(request):
    programs=Program.objects.all()

    return render(request, "students/program.html",{
        "programs":programs,
    })

def add_programme(request):

    if request.method =="POST":
        form=ProgrammeForm(request.POST)
        if form.is_valid():

            prog_code=form.cleaned_data['prog_code']
            prog_name=form.cleaned_data['prog_name']

            new_pro=Program(prog_code=prog_code,prog_name=prog_name)

            new_pro.save()

            return render(request, "students/add_program.html",{
                "form":ProgrammeForm(),
                "success":True,"message":"Program added successfully"
            })
            
        else:
            return render(request, "students/add_program.html",{
                "form":ProgrammeForm(),
                "success":True,"message":"failed to add program"
            })
    else:
        form=ProgrammeForm()

        return render(request, "students/add_program.html",{
            "form":form
        })
def admission(request):
    if request.method =="POST":
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            student=form.save(commit=False)
            print("saving.............")
            
            student.save()
            return render(request,"students/admissions.html",{"form":StudentForm(),"success":True,"message":"Saved Successfully "})
        return render(request,"students/admissions.html",{"form":StudentForm(),"message":"Failed to save "})
           
    else:
        form=StudentForm()
        
        return render(request,"students/admissions.html",{"form":form})

def students(request):
    if request.method =="POST":
        prog=request.POST['prog']
        search=request.POST['search']
        if prog =="All":
            students=Student.objects.filter((Q(surname__icontains=search) | Q(othernames__icontains=search) | Q(student_no__contains=search)))
        else:
         students=Student.objects.filter((Q(surname__icontains=search) | Q(othernames__icontains=search) | Q(student_no__contains=search)) , prog_code=prog)
         
        student_serialized=serializers.serialize('json',students) 
        return HttpResponse(student_serialized)
        
    else:
        students=Student.objects.all()
        programs=Program.objects.all()
        
        
        return render(request,"students/students.html",{"students":students,"programs":programs})

def edit_student(request,pro):
    student=Student.objects.get(student_id=pro)
    url=student.image.url
    if request.method =="POST":
        delete_file(request,student.image.url)
        form=StudentForm(request.POST,request.FILES,instance=student)
        form.save()
        student=Student.objects.get(student_id=pro)
        url=student.image.url
        return render(request,"students/edit_student.html",{"form":StudentForm(instance=student),"success":True,"url":url})
    else:
        form=StudentForm(instance=student)
        return render(request,"students/edit_student.html",{"form":form,"url":url})
    
def delete_student(request,id):
    student=Student.objects.get(_id=id)
    delete_url=os.path.join(settings.BASE_DIR,"media","uploads",os.path.basename(student.image.url))
    os.remove(delete_url)
    student.delete()
    return HttpResponseRedirect(reverse("view_students"))

def Single_student(request,id):
    if id is not None:
        
        student=Student.objects.get(pk=id)
        ac=Academic_year.objects.filter(Q(status__contains='Active'))[0]
        if ac is not None:
            # session=Session.objects.get(student=student,academic_year=ac)
            courses=Course.objects.filter(prog_code=student.prog_code)
            return render(request,"students/Student.html",{"student":student,'courses':courses})