# Generated by Django 3.2.25 on 2024-07-08 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainshop', '0011_alter_article_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='gnp',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='country',
            name='gnp_per_capita',
            field=models.BigIntegerField(default=0),
        ),
    ]
