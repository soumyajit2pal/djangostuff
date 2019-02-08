from django.contrib import admin
from appTwo.models import Users
# Register your models here.

class UserView(admin.ModelAdmin):
    list_display=['first_name','last_name','email']

admin.site.register(Users,UserView)