from django.contrib import admin
from .models import Course,Student,Program,Academic_year,Semester
# Register your models here.
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Program)
admin.site.register(Academic_year)
admin.site.register(Semester)