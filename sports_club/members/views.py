from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# Members view 
def members(request):
    template = loader.get_template("welcome.html")
    return HttpResponse(template.render())

# Sample view
def sample(request):
    template = loader.get_template("sample.html")
    return HttpResponse(template.render())

# Worksheet13 view
def worksheet13(request):
    template = loader.get_template("worksheet13.html")
    return HttpResponse(template.render())
    