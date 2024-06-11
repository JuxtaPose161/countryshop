from django.urls import path
from . import views

urlpatterns = [
    path('shop', views.main_page, name='shop'),
    path('', views.to_need_page)
]
