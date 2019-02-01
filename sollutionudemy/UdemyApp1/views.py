from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("You are in Home page")
def map(request):
    reg_d={'reg_page':""}
    return render(request,'UdemyApphtml/home.html',context=reg_d)