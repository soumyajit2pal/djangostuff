from django.shortcuts import render
from  . import form
# Create your views here.

def index(request):
    return render(request,"testapp/index.html")

def form_name_view(request):
    form_data=form.FormName()
    if request.method=="POST":
        form_data=form.FormName(request.POST)

        if form_data.is_valid():
            print("Valid succesfull")
            print("Name "+form_data.cleaned_data['name'])
            print("Email "+form_data.cleaned_data['email'])
            print("Text "+form_data.cleaned_data['text'])


    return render(request,"testapp/form_page.html",{"form":form_data})

  