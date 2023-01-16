from django.shortcuts import render,redirect
from eshopapp.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from eshopapp.models.order import Order
from django.utils.decorators import method_decorator
from eshopapp.middlewares.auth import auth_middleware

class OrderView(View):
    @method_decorator(auth_middleware)
    def get(self, request):
        customer=request.session.get('customer')
        orders=Order.get_oders_by_customer_id(customer)
        return render(request,"order.html",{'orders':orders})