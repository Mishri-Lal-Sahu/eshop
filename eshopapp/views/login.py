from django.shortcuts import render,redirect
from eshopapp.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View

class Login(View):
    def get(self,request):
       return render(request,"login.html")
    def post(self,request):
        email=request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email_address(email)
        error = None
        if customer:
            flag = check_password(password , customer.password)
            if flag:
                request.session['customer']=customer.id
                request.session['customer_name']=customer.first_name
                return redirect('homepage')
            else:
                error = "Password invalid!"
        else:
            error = "This email is not exist.!"
        return render(request,"login.html",{'error':error})

def logout(request):
    request.session.clear()
    return redirect('login')