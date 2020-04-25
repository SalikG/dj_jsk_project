from django.urls import path
from . import views

app_name = 'product_management_app'

urlpatterns = [
    path('', views.index, name="shopping"),
    path('addToCart/', views.add_product_to_cart, name="add_to_cart"),
    path('subProductFromCart/', views.sub_or_remove_order_item, name="sub_or_remove_order_item"),
]
