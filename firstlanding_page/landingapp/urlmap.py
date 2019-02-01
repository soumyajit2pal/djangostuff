from django.http import HttpResponse
from django.urls import path
from landingapp import views

urlpatterns=[
    path('',views.date_time,name='datetime'),
]
