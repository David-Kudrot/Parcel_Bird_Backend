from django.db import models
from product.models import *
from User.models import User
from django.utils import timezone

# Create your models here.

class Order(models.Model):
    Category=(
        ('just_placed','just_placed'),
        ('on_process','on_process'),
        ('on_delivery','on_delivery'),
        ('delivered','delivered'),
             )
    
    user=models.ForeignKey(User,on_delete=models.PROTECT,related_name='user_order')
    products=models.ManyToManyField(CartItem,related_name='product_order')
    total_cost=models.DecimalField(max_digits=10, decimal_places=2)
    status=models.CharField(max_length=20,choices=Category)
    ordered_at = models.DateTimeField(auto_now_add=True)
    delivery_at=models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return f'{self.user} {self.products} {self.total_cost} {self.status}'    