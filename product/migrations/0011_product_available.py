# Generated by Django 5.0.6 on 2024-05-25 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_product_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]