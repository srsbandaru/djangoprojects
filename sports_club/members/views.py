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
    message = "This content is coming from sample view of members application"
    return HttpResponse(message)