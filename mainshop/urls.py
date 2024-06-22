from django.urls import path
from . import views

urlpatterns = [
    path('shop', views.main_page, name='shop'),
    path('', views.to_need_page),
    path('shop/score/<level>', views.score_sorted_main_page, name ='shop_score'),
    path('shop/color/<color>', views.color_sorted_main_page, name ='shop_color'),
]
