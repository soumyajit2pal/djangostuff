from django.contrib import admin
from testapp.models import reminder
# Register your models here.
class showData(admin.ModelAdmin):
    list_display=['name','purpose','dosage','date']
admin.site.register(reminder,showData)