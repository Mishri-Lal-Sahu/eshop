from django.contrib import admin
from django.urls import path
from eshopapp.views import home,signup,login,cart,checkout,order,adminLogin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/login', auth_views.LoginView.as_view(template_name='adminLogin.html'), name='adminLogin'),
    path('',home.index.as_view(),name="homepage"),
    path('signup',signup.Signup.as_view(),name="signup"),
    path('login',login.Login.as_view(),name="login"),
    path('logout',login.logout,name="logout"),
    path('cart',cart.Cart.as_view(), name="cart"),
    path('checkout',checkout.Checkout.as_view(), name="checkout"),
    path('order', order.OrderView.as_view(), name="order")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)