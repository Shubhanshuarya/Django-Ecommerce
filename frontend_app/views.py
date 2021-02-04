from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'frontend_app/home.html')


def product_detail(request):
    return render(request, 'frontend_app/productdetail.html')
