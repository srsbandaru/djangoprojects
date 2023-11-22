from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
# Members view 
# def members(request):
#    template = loader.get_template("welcome.html")
#    return HttpResponse(template.render())
def members(request):
    myMembers = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        "membersList":myMembers
    }
    return HttpResponse(template.render(context, request))

# Sample view
def sample(request):
    template = loader.get_template("sample.html")
    return HttpResponse(template.render())

# Worksheet13 view
def worksheet13(request):
    template = loader.get_template("worksheet13.html")
    return HttpResponse(template.render())
    