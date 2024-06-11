# Generated by Django 3.2.25 on 2024-06-07 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='code',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='flag_path',
            field=models.ImageField(null=True, upload_to='flags/'),
        ),
        migrations.AddField(
            model_name='country',
            name='slug',
            field=models.SlugField(default='', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='gnp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='country',
            name='gnp_per_capita',
            field=models.IntegerField(default=0),
        ),
    ]
