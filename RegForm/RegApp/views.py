from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    my_dic={'reg_page':""}
    return render(request,'registration.html',context=my_dic)