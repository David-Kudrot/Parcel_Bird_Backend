from django.db import models
from User.models import RiderProfile,User
from purchase.models import Order

# Create your models here.


class Customer_review(models.Model):
    rider=models.ForeignKey(RiderProfile,on_delete=models.PROTECT)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    review_message=models.TextField(blank=True,null=True)
    rating=models.FloatField()
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.customer} - {self.rider}'
    

class Customer_History(models.Model):
    customer=models.OneToOneField(User,on_delete=models.PROTECT)
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    order_time=models.DateTimeField()
    delivery_time=models.DateTimeField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    points=models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.customer.email} - {self.points}'
