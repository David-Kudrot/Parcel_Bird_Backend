# Generated by Django 5.0.6 on 2024-06-01 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0008_order_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='transactionId',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
