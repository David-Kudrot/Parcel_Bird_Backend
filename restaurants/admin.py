from django.contrib import admin
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',  'latitude', 'longitude')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Restaurant, RestaurantAdmin)
