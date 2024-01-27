from django.urls import path
from . import views

urlpatterns=[
    path("staffs/",views.staffs,name="staffs"),
    path("staffs/edit/<int:id>",views.edit_staff,name="edit_staff"),
    path("faculty/all",views.view_faculty,name="view_faculty"),
]