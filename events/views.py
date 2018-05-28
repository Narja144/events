from django.shortcuts import render # origin line
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hey Client, my app is running!")
