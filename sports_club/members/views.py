from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Members view 
def members(request):
    message = "I sang the whole Hanuman Chalisa in Hindi"
    return HttpResponse(message)
    
