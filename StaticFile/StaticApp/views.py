from django.shortcuts import render
from StaticApp import views
from django.http import HttpResponse
# Create your views here.
def index(request):
    
    return render(request,"StaticApp/index.html",context=None)