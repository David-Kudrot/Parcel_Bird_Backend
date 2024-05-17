# Generated by Django 5.0.6 on 2024-05-16 17:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliverystatus', models.CharField(blank=True, choices=[('onprocessing', 'On Processing'), ('delivered', 'Delivered')], max_length=30, null=True)),
                ('orderstatus', models.CharField(blank=True, choices=[('received', 'Received'), ('rejected', 'Rejected')], max_length=30, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('receive', models.CharField(blank=True, choices=[('received', 'Received'), ('notreceived', 'Not Received')], max_length=40, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]