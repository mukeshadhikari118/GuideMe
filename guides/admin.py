from django.contrib import admin
from .models import guide


class guideAdmin(admin.ModelAdmin):  
  list_display = ('first_name', 'last_name', 'contact','address1','address2','email','password','bio','pan','pp','citizenship') 

# Register your models here.
admin.site.register(guide, guideAdmin) 

