import datetime

from django.db import models
from.product import Product
from.customer import Customer
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address=models.CharField(max_length=50,default='')
    phone=models.CharField(max_length=50,default='')
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_oders_by_customer_id(customer_id):
        return Order.objects.filter(customer_id=customer_id).order_by('-date')