from django.shortcuts import render
from django.http import HttpResponse,Http404
import json
# Create your views here.
from .models import Form;

def data(request):
    if request.method == "POST":
        return Http404({"form":"page not found"})
    return HttpResponse("hello")
def post_data(request):
    if request.method == "POST":
        form=request.POST
        print(form)
        return HttpResponse("request made")
    else:
        return HttpResponse("No data submitted ..")
        
        