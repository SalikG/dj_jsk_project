
from django.db import models
from login_app.models import UserProfile


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=0, default=0)

    def __str__(self):
        return f'{self.name} - {self.price}'


class Storage(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Stock(models.Model):
    storage = models.ForeignKey(Storage, related_name='in_stock', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='in_stock', on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.product} - {self.quantity}'


class Order(models.Model):
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.ForeignKey(UserProfile, related_name='order', on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.total_price} - {self.user} - {self.timestamp}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_item', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order', on_delete=models.PROTECT)
    quantity = models.IntegerField()
    total_discount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.product} - {self.order} - {self.quantity} - {self.total_discount}'


class Deal(models.Model):
    product = models.ForeignKey(Product, related_name='discount', on_delete=models.CASCADE)
    discount_persentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.product} - {self.discount_persentage} - {self.start_date} - {self.end_date}'
