from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def template_view(request):
    
    return render(request,'testapp/results.html')
def time_date(request):
    date_time=datetime.datetime.now()
    mydic={"date":date_time}
    return render(request,'testapp/results.html',context=mydic)