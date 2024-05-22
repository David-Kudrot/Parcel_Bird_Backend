from django.contrib import admin
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'total_product_count', 'latitude', 'longitude')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('products',)

    def total_product_count(self, obj):
        return obj.total_product_count()
    total_product_count.short_description = 'Total Products'

admin.site.register(Restaurant, RestaurantAdmin)
