from django.db import models
from django.utils.text import slugify
class Country(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, default='')
    gnp = models.IntegerField(default=0)
    gnp_per_capita = models.IntegerField(default=0)
    code = models.CharField(max_length=2, null=True)
    flag_path = models.ImageField(upload_to='flags/', null=True)
    tags = models.ManyToManyField('Tags', blank=True, related_name='tags')
    is_sale = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.flag_path = f'flags/{self.code}.png'
        super(Country, self).save(*args, **kwargs)

class Tags(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, default='')
    group = models.ForeignKey('TagsGroup', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tags, self).save(*args, **kwargs)

class TagsGroup(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, default='')

    def __str__(self):
        return str(self.name)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(TagsGroup, self).save(*args, **kwargs)