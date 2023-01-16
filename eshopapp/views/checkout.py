from django.shortcuts import redirect
from django.views import View
from eshopapp.models.product import Product
from eshopapp.models.order import Order
from eshopapp.models.customer import Customer

class Checkout(View):
    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))
        print(address,phone,customer,cart,products)

        for product in products:
            order=Order(customer_id =Customer(id=customer),
                        product=product,
                        price=product.price,
                        address=address,
                        phone=phone,
                        quantity=cart.get(str(product.id)))
            order.placeOrder()
            request.session['cart'] = {      }
        return redirect('cart')