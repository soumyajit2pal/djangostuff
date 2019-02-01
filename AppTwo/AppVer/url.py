from django.urls import path
from AppVer import views
urlpatterns=[
    path('',views.index,Name='index'),
]