# Generated by Django 3.2.25 on 2024-07-01 14:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainshop', '0007_auto_20240701_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='creating_date',
            field=models.DateTimeField(default=django.utils.timezone.localtime),
        ),
    ]