from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, common_name, description, weight):
    self.name = name
    self.common_name = common_name
    self.description = description
    self.weight = weight

finches = [
  Finch('Lolo', 'Hawaiian Honeycreeper', 'Dark red with long, curved bill', 13),
  Finch('Sachi', 'Rosefinch', 'Red and plump', 24),
  Finch('Raven', 'Desert Finch', 'yellowish', 25)
]

def home(request):
    return HttpResponse('<h1>Hello Finches</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', { 'finches': finches })