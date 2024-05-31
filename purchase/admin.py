from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Order)
class Orderadmin(admin.ModelAdmin):
    list_display=['id','user','total_cost','status']
    
    def products(self):
        pass