from rest_framework import serializers

from mainshop.models import Country, FlagColors
from django.contrib.auth.models import User

class MyRelatedField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        return str(value)

class CountrySerializers(serializers.ModelSerializer):
    flag_colors = MyRelatedField(many=True, queryset=FlagColors.objects.all())

    class Meta:
        model = Country
        fields = ('name', 'gnp', 'gnp_per_capita', 'is_sale', 'flag_colors')

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'is_active')