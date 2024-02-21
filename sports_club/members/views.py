from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import MemberForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

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
# def create_member(request):
#     template = "member_form.html"
#     form = MemberForm()
#     context = {
#         'form':form
#     }
#     return render(request, template, context)

# Create Member
class create_member(LoginRequiredMixin, View):
    template = "member_form.html"
    success_url = "members:main"

    def get(self, request):
        form = MemberForm()
        context = {
            'form':form
        }
        return render(request, self.template, context)
    def post(self, request):
        form = MemberForm(request.POST)
        if not form.is_valid():
            context = {
                'form':form
            }
            return render(request, self.template, context)
        form.save()
        return redirect(self.success_url)
    
# Update member
class update_member(LoginRequiredMixin, View):
    model = Member
    template = "member_form.html"
    success_url = "members:members"

    def get(self, request, pk):
        member = get_object_or_404(self.model, id=pk)
        form = MemberForm(instance=member)
        context = {
            'form':form
        }
        return render(request, self.template, context)
    def post(self, request, pk):
        member = get_object_or_404(self.model, id=pk)
        form = MemberForm(request.POST, instance=member)
        if not form.is_valid():
            context = {
                'form':form
            }
            return render(request, self.template, context)
        form.save()
        return redirect(self.success_url)

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

    