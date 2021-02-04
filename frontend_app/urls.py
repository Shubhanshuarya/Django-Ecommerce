from django.urls import path
from frontend_app import views

urlpatterns = [
    path('', views.home),
    path('product-detail/', views.product_detail, name="product-detail"),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),

]