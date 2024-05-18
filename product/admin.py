from django.contrib import admin
from .models import Product, Category, CartItem, CustomerAddress

# Register Product model with admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'date']
    list_filter = ['date']
    search_fields = ['name', 'description']

# Register Category model with admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'slug']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}  # Auto-populate slug field based on title


class CardItemAdim(admin.ModelAdmin):
    list_display = ['id','user', 'product','quantity']

admin.site.register(CartItem, CardItemAdim)



class CustomerAddressAdin(admin.ModelAdmin):
    list_display = ['id', 'user', 'recipient_name']
admin.site.register(CustomerAddress, CustomerAddressAdin)
