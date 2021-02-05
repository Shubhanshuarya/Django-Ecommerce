from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced


# def home(request):
#    return render(request, 'frontend_app/home.html')
class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        return render(request, 'frontend_app/home.html', {'topwears': topwears, 'bottomwears': bottomwears, 'mobiles': mobiles})


# def product_detail(request):
#     return render(request, 'frontend_app/productdetail.html')

class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'frontend_app/productdetail.html', {'product': product})


def add_to_cart(request):
    return render(request, 'frontend_app/addtocart.html')


def buy_now(request):
    return render(request, 'frontend_app/buynow.html')


def profile(request):
    return render(request, 'frontend_app/profile.html')


def address(request):
    return render(request, 'frontend_app/address.html')


def orders(request):
    return render(request, 'frontend_app/orders.html')


def change_password(request):
    return render(request, 'frontend_app/changepassword.html')


def mobile(request):
    return render(request, 'frontend_app/mobile.html')


def login(request):
    return render(request, 'frontend_app/login.html')


def customer_registration(request):
    return render(request, 'frontend_app/customerregistration.html')


def checkout(request):
    return render(request, 'frontend_app/checkout.html')
