from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def nextPage(request):
    return HttpResponse('<h1>namaste means Hello in india</h1>')
