from django.urls import path
from .views import *
urlpatterns=[
    path("data/",data,name="data_upload"),
    path("post/data",post_data,name="post_data"),
]