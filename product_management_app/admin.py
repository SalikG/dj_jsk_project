from django.contrib import admin
from .models import Product, Storage, Order, OrderItem, Stock, Deal
# Register your models here.

admin.site.register(Product)
admin.site.register(Storage)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Stock)
admin.site.register(Deal)