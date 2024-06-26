# Generated by Django 5.0.6 on 2024-05-31 16:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_cartitem_product'),
        ('purchase', '0005_rename_product_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='order', to='product.cartitem'),
        ),
    ]
