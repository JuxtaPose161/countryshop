from rest_framework import serializers

from mainshop.models import Country, FlagColors, Article, Cart
from django.contrib.auth.models import User

class MyRelatedField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        return str(value)

class CountrySerializers(serializers.ModelSerializer):
    flag_colors = MyRelatedField(many=True, queryset=FlagColors.objects.all())
    class Meta:
        model = Country
        fields = ('name', 'gnp', 'gnp_per_capita', 'is_sale', 'flag_colors')
class ArticleSerializers(serializers.ModelSerializer):
    owner = MyRelatedField(queryset=User.objects.all())
    country = serializers.SlugRelatedField(queryset=Country.objects.all(), slug_field='slug')
    class Meta:
        model = Article
        fields = ('owner', 'country', 'article', 'creation_data')

class CartSerializers(serializers.ModelSerializer):
    purchases = MyRelatedField(many=True, queryset=Country.objects.all())
    class Meta:
        model = Cart
        fields = ('purchases', 'cash', 'creating_date')
class UserSerializers(serializers.ModelSerializer):
    cart = CartSerializers()
    class Meta:
        model = User
        fields = ('username', 'cart', 'is_active')