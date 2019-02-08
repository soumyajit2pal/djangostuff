from appTwo import views
from django.urls import path

urlpatterns=[
    path("",views.user_detail, name="signup")
]