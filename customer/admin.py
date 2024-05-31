from django.contrib import admin
from .models import Customer_review, Customer_History

# Register your models here.

@admin.register(Customer_review)
class CustomerReviewAdmin(admin.ModelAdmin):
    list_display = ('id','rider', 'customer', 'order', 'rating', 'date')
    list_filter = ('rider', 'customer', 'order', 'date')
    search_fields = ('rider__name', 'customer__username', 'order__id')

@admin.register(Customer_History)
class CustomerHistoryAdmin(admin.ModelAdmin):
    list_display = ('id','customer', 'order', 'order_time', 'delivery_time', 'price', 'points')
    list_filter = ('customer', 'order_time', 'delivery_time')
    search_fields = ('customer__username', 'order__id')

