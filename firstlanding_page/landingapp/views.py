from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime
def index(request):
    return render(request,"landingpage/index.html")

def date_time(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))

    if h<12:
        msg="Yaa Good Morning"
    elif(h<16):
        msg="Ya Good Afternoon"
    elif(h<21):
        msg="Ya Good Evening"
    else:
        msg="Ya Good Night"
    mydict={'date':date, 'msg':msg}

    return render(request,"landingpage/index.html",mydict)