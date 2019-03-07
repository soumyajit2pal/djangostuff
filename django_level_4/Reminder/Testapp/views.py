from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def  addZero(hr):
    if(int(hr)<10):
        return "0"+hr
    else:
        return hr
def index(request):
    time=""
    if request.method=="POST":
        hr=request.POST['hour']
        min=request.POST['minutes']
        sec=request.POST['seconds']
        print(addZero(hr))
        print(addZero(min))
        print(addZero(sec))
        time=addZero(hr)+":"+addZero(min)+":"+addZero(sec)
    return render(request,'Testapp/index.html',{"hr":range(24),"min":range(60),"sec":range(60),"times":time})