from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def homefunction(request):
    return HttpResponse("ahi")


def aboutfunction(request):
    return render(request,'home.html')

