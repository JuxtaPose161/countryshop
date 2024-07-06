from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='shop'),
    path('score/<level>', views.score_sorted_main_page, name = 'shop_score'),
    path('color/<color>', views.color_sorted_main_page, name = 'shop_color'),
    path('article/<slug:country>', views.country_article_page, name = 'shop_article'),
    path('cart', views.user_cart_page, name = 'cart'),
    path('pic/<slug:country>', views.put_in_cart, name = 'pic'),
    path('write_article/<slug:country>', views.create_article, name = 'create_article'),
    path('update_article/<slug:country>', views.update_article, name = 'update_article'),
    path('delete_article/<slug:country>', views.delete_article, name = 'delete_article'),
]
