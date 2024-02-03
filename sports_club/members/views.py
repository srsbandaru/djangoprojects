from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import MemberForm

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
def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

# create member view
def create_member(request):
    template = "member_form.html"
    form = MemberForm()
    context = {
        'form':form
    }
    return render(request, template, context)

# test view
def test(request):
    myMembers = Member.objects.all().values()
    template = loader.get_template("test.html")
    context = {
        'myMembers':myMembers,
        'firstName':"Sriram Surya",
        'lastName':"Bandaru",
        'greeting':0,
        'languagesKnown':["English", "Telugu"],
        'list_1':["Coding", "Reading"],
        'list_2':["Coding", "Reading"],
        'cars':[
            {
                'brand':'Subaru',
                'model':'WRX',
                'year': 1964
            },
            {
                'brand':'Hyundai',
                'model':'Palaside',
                'year':1996
            },
            {
                'brand':'KIA',
                'model':'Carnival',
                'year':1986
            }
        ],
        'hobbies':["Watching Cricket", "Playing Piano", "Swimming", "Listening to music"],
        'favourites':[]
        
    }

    return HttpResponse(template.render(context, request))

    