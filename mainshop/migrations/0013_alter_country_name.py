# Generated by Django 3.2.25 on 2024-07-08 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainshop', '0012_auto_20240708_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=35, unique=True),
        ),
    ]
