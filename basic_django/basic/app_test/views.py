from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<html><body><h1>Hello World!</h1></body></html')
