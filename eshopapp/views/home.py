from django.shortcuts import render,redirect
from django.http import HttpResponse
from eshopapp.models.product import Product
from eshopapp.models.category import Category
from django.views import View

# Create your views here.
class index(View):
    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1
                else:
                    cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart
        return redirect('homepage')

    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart']={}
        products = None
        category = Category.get_all_category()
        categoryId = request.GET.get('category')
        if categoryId:
            products = Product.get_all_product_by_id(categoryId)
        else:
            products = Product.get_all_product()
        data = {}
        data['product'] = products
        data['category'] = category
        return render(request, "index.html", data)