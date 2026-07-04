from django.urls import path
from . import views


urlpatterns = [
    path('products_list/', views.cart_view, name='cart'),
    path('categories_list/', views.categ_view, name='categs'),
]