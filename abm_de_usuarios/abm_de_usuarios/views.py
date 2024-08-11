from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return HttpResponse("login en construccion")


def home(request):
    return render(request,'home.html',{})