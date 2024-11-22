from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

# def sayHi(request):
#     return render(request , 'home.html')

class messageView(TemplateView):
    template_name = "home.html"

class aboutView(TemplateView):
    template_name = "about.html"