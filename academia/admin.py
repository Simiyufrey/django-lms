from django.contrib import admin
from .models import Lecture, Enrollment,ClassR

# Register your models here.
admin.site.register([Lecture,Enrollment,ClassR])

