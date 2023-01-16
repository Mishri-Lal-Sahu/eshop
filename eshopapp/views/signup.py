from django.shortcuts import render,redirect
from eshopapp.models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View


class Signup(View):
    def get(self,request):
       return render(request,"signup.html")
    def post(self,request):
        customerData = request.POST
        first_name = customerData.get('firstname')
        last_name = customerData.get('lastname')
        phone_number = customerData.get('number')
        email_address = customerData.get('email')
        password = customerData.get('password')
        # value store
        customer = Customer(first_name=first_name, last_name=last_name, phone_number=phone_number,
                            email_address=email_address, password=password)
        customer.password = make_password(customer.password)
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'email_address': email_address
        }
        error = self.validate(customer)
        if error == None:
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error,
                'value': value
            }
            return render(request, "signup.html", data)

    def validate(self,customer):
        error = None
        if not customer.first_name:
            error = "First name is required!"
        elif len(customer.first_name) < 4:
            error = "First name must be greter than 4 latter!"
        elif not customer.last_name:
            error = "Last name is required!"

        elif len(customer.last_name) < 4:
            error = "Last name must be greter than 4 latter!"
        elif not customer.phone_number:
            error = "Phone number is required!"
        elif not len(customer.phone_number) == 10:
            error = "Phone number must be equal to 10 digit!"
        elif not customer.email_address:
            error = "Email address is required!"
        elif not customer.password:
            error = "Password is required!"
        elif len(customer.password) < 8:
            error = "Password must be greater than 7 latter!"
        elif customer.isExist():
            error = "This email address already exist.."
        return error