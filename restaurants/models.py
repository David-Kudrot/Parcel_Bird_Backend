from django.db import models
from django.utils.text import slugify
from product.models import Product


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    products = models.ManyToManyField(Product, related_name='restaurants')
    image = models.ImageField(upload_to='restaurant_images/', null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Restaurant, self).save(*args, **kwargs)

    def total_product_count(self):
        return self.products.count()

    def __str__(self):
        return self.name
