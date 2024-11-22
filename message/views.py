from django.shortcuts import render
from django.views.generic import ListView
from .models import testDataBase
# Create your views here.

# def sayHi(request):
#     return render(request , 'home.html')

class messageView(ListView):
    model = testDataBase
    template_name = "home.html"

class aboutView(ListView):
    model = testDataBase
    template_name = "about.html"