from django.db import models
from django.utils.text import slugify
from User.models import User

# Category Model
class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        # Auto-generate slug from the title
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.name
    



class CartItem(models.Model):
    DELIVERY_STATUS_CHOICES = [
        ('onprocessing', 'On Processing'),
        ('delivered', 'Delivered'),
    ]

    RECEIVE_STATUS_CHOICES = [
        ('received', 'Received'),
        ('notreceived', 'Not Received'),
    ]

    ORDER_STATUS_CHOICES = [
        ('received', 'Received'),
        ('rejected', 'Rejected'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    deliverystatus = models.CharField(max_length=30, choices=DELIVERY_STATUS_CHOICES, null=True, blank=True)
    orderstatus = models.CharField(max_length=30, choices=ORDER_STATUS_CHOICES, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(null=True, blank=True)
    receive = models.CharField(max_length=40, choices=RECEIVE_STATUS_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.product.name
