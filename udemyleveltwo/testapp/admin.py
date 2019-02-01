from django.contrib import admin
from testapp.models import User
# Register your models here.

class adminuser(admin.ModelAdmin):
    list_display=['first_name','last_name','email']

admin.site.register(User,adminuser)
