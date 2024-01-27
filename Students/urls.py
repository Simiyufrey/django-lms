from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("add/",views.courses,name="add_course"),
    path("student/edit/<int:pro>",views.edit_student,name="edit_student"),
    path("course/delete/<str:id>",views.delete_course,name="delete_course"),
    path("student/delete/<int:id>",views.delete_student,name="delete_student"),
    path("programs/",views.programs,name="programs"),
    path("programs/add",views.add_programme,name="addprogram"),
    path("students/add",views.admission,name="add_student"),
    path("student/<int:id>/view",views.Single_student,name='view_student'),
    path("students/all",views.students,name="view_students"),
    path("courses/<str:pro>",views.view_course,name="view_courses"),
]