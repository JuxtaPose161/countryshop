from django.db import models
from django.utils.text import slugify
class Country(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, default='')
    gnp = models.IntegerField(default=0)
    gnp_per_capita = models.IntegerField(default=0)
    code = models.CharField(max_length=2, null=True)
    flag_colors = models.ManyToManyField('FlagColors', related_name='colors')
    flag_path = models.ImageField(upload_to='flags/', null=True)
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
