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

# details view
def details(request, id):
    myMember = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        "myMember":myMember
    }
    return HttpResponse(template.render(context, request))

# main view
def main(reqeust):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())