from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
class Country(models.Model):
    name = models.CharField(max_length=35, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, default='')
    gnp = models.BigIntegerField(default=0)
    gnp_per_capita = models.BigIntegerField(default=0)

    code = models.CharField(max_length=2, null=True)
    flag_colors = models.ManyToManyField('FlagColors', related_name='colors')
    flag_path = models.ImageField(upload_to='flags/', null=True)

    price = models.DecimalField(max_digits=7, decimal_places=2, default=1000)
    is_sale = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = slugify(self.name)
            self.flag_path = f'flags/{self.code}.png'
        super(Country, self).save(*args, **kwargs)

class FlagColors(models.Model):
    name = models.CharField(max_length=30, db_index=True, unique=True)
    def __str__(self):
        return self.name

class Article(models.Model):
    owner = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, related_name='article')
    article = models.TextField()
    country = models.ForeignKey(Country, models.CASCADE, related_name='about')
    creation_data = models.DateTimeField(default=timezone.localtime)

    def __str__(self):
        return f'{self.owner if not None else "Admin"} article about {self.country}'

class Cart(models.Model):
    owner = models.OneToOneField(User, models.CASCADE, primary_key=True, related_name='cart')
    purchases = models.ManyToManyField(Country)
    cash = models.IntegerField(default=0)
    creating_date = models.DateTimeField(default=timezone.localtime)
    def __str__(self):
        return f'{self.owner} cart'