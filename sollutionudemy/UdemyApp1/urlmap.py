from django.http import HttpResponse
from django.urls import path
from UdemyApp1 import views

urlpatterns=[
    path('',views.map,name='Map'),
]