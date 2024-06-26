# Generated by Django 5.0.6 on 2024-05-29 23:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0006_alter_riderprofile_user'),
        ('customer', '0001_initial'),
        ('purchase', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_history',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='purchase.order'),
        ),
        migrations.AddField(
            model_name='customer_review',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customer_review',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.order'),
        ),
        migrations.AddField(
            model_name='customer_review',
            name='rider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='User.riderprofile'),
        ),
    ]
