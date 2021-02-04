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
