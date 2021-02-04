from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'frontend_app/home.html')


def product_detail(request):
    return render(request, 'frontend_app/productdetail.html')


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
