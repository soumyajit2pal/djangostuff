from django.contrib import admin
from firstapp.models import Topic, AccessRecord, Webpage
# Register your models here.

class web(admin.ModelAdmin):
    list_display=['name','url']

class topic(admin.ModelAdmin):
    list_display=['top_name']
    
admin.site.register(Topic,topic)
admin.site.register(AccessRecord)
admin.site.register(Webpage,web)
