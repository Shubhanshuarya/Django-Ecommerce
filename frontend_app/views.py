from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .forms import CustomerRegistrationForm, CustomerProfileForm
from .models import Customer, Product, Cart, OrderPlaced
from django.conf import settings
from django.core.mail import send_mail


# def home(request):
#    return render(request, 'frontend_app/home.html')
class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        return render(request, 'frontend_app/home.html',
                      {'topwears': topwears, 'bottomwears': bottomwears, 'mobiles': mobiles})


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


# def profile(request):
#     return render(request, 'frontend_app/profile.html')

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'frontend_app/profile.html', {'form': form})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations!! Profile Updated Successfully.')
        return render(request, 'frontend_app/profile.html', {'form': form})


def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'frontend_app/address.html', {'add': add})


def orders(request):
    return render(request, 'frontend_app/orders.html')


def mobile(request, data=None):
    if data is None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'Redmi' or data == 'Samsung':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'below-15000':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=15000)
    elif data == 'above-15000':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=15000)
    return render(request, 'frontend_app/mobile.html', {'mobiles': mobiles})


# def login(request):
#     return render(request, 'frontend_app/login.html')


# def customer_registration(request):
#     return render(request, 'frontend_app/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'frontend_app/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_email = form.cleaned_data['email']
            messages.success(request, 'Congratulations!! Registered Successfully.')
            form.save()
            subject = 'Welcome to V-Mart Shopping Mall'
            message = f'Hi {user_name}, Thank you for registering in V-Mart. We will serve you best services and best deals as well.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user_email, ]
            send_mail(subject, message, email_from, recipient_list)
        return render(request, 'frontend_app/customerregistration.html', {'form': form})


def checkout(request):
    return render(request, 'frontend_app/checkout.html')
