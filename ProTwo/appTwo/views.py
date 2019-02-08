from django.shortcuts import render
from django.http import HttpResponse
from appTwo.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request,"appTwo/index.html")

def user_detail(request):
    form=NewUserForm()

    if request.method=='POST':
        form=NewUserForm(request.POST)

        if(form.is_valid()):
            form.save(commit=True)
            return index(request)
        else:
            print("form invlid")
    return render(request,"appTwo/users.html",{'form':form})