from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .permisions import IsAdminUserOrReadOnly
from mainshop.models import Country, Article
from .serializers import *
from django.contrib.auth.models import User


class CountryAPIView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers
    permission_classes = (IsAdminUserOrReadOnly, )
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    permission_classes = (IsAdminUserOrReadOnly, )
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsAdminUser, )