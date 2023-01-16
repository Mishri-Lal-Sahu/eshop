from django.shortcuts import render,redirect
from eshopapp.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from eshopapp.models.product import Product

class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        product=Product.get_product_by_id(ids)
        return render(request,"cart.html",{'product':product})