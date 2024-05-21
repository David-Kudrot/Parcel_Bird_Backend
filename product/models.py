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
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name





class CustomerAddress(models.Model):
    id = models.IntegerField(primary_key=True)
    delivary_boy = models.CharField(max_length=50 ,null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    recipient_name = models.CharField(max_length=255, null=True, blank=True)
    street_address = models.CharField(max_length=255, null=True, blank=True)
    apartment_address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    county = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return f"{self.recipient_name}, {self.street_address}, {self.city}, {self.state}, {self.postal_code}"
