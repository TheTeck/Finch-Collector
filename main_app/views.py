from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello Finches</h1>')

def about(request):
    return render(request, 'about.html')