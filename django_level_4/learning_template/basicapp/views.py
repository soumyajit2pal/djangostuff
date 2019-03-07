from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context_dic={"text":"Hello World","Number":100}
    return render(request,"basicapp/index.html", context_dic)

def other(request):
    return render(request,"basicapp/other.html")

def relative (request):
    return render(request,"basicapp/relative_url_template.html")