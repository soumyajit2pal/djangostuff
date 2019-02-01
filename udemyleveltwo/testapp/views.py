from django.shortcuts import render

# Create your views here.
from testapp.models import User

def index(request):
    return render(request,'testapp/index.html')

def users(request):
    user=User.objects.order_by('first_name')
    return render(request,'testapp/users.html',{'user_dict':user})