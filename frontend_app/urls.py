from django.urls import path, include
from frontend_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
                  path('', views.ProductView.as_view(), name="home"),
                  path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name="product-detail"),
                  path('search', views.SearchPage, name='search_result'),
                  ####################################################
                  # Add to Cart and Buy Now Functionality
                  path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
                  path('cart/', views.show_cart, name='show_cart'),
                  path('pluscart/', views.plus_cart),
                  path('minuscart/', views.minus_cart),
                  path('removecart/', views.remove_cart),
                  path('checkout/', views.checkout, name='checkout'),
                  path('paymentdone/', views.payment_done, name='paymentdone'),
                  path('orders/', views.orders, name='orders'),

                  # ProfilePage View
                  path('profile/', views.ProfileView.as_view(), name='profile'),
                  path('address/', views.address, name='address'),
                  # Urls for Mobile Classified Separate Product Page
                  path('mobile/', views.mobile, name='mobile'),
                  path('mobile/<slug:data>', views.mobile, name='mobile_data'),

                  #################################################################
                  # User Authentication, Password Change, Reset Form and Many more... related to User Auth
                  path('accounts/login/', auth_views.LoginView.as_view(template_name='user_auth/login.html',
                                                                       authentication_form=LoginForm), name='login'),
                  path('registration/', views.CustomerRegistrationView.as_view(), name='customer_registration'),
                  path('activate/<uidb64>/<token>/',views.activate, name='activate'),
                  path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
                  path('password_change/',
                       auth_views.PasswordChangeView.as_view(template_name='user_auth/password_change.html',
                                                             form_class=MyPasswordChangeForm), name="password_change"),
                  path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
                      template_name='user_auth/password_change_done.html'), name="password_change_done"),

                  path('password_reset/',
                       auth_views.PasswordResetView.as_view(template_name='user_auth/password_reset.html',
                                                            form_class=MyPasswordResetForm), name="password_reset"),
                  path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
                      template_name='user_auth/password_reset_confirm.html', form_class=MySetPasswordForm),
                       name="password_reset_confirm"),
                  path('password_reset/done/',
                       auth_views.PasswordResetDoneView.as_view(template_name="user_auth/password_reset_done.html"),
                       name="password_reset_done"),
                  path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
                      template_name="user_auth/password_reset_complete.html"), name="password_reset_complete"),

                  path('oauth/', include('social_django.urls', namespace='social')),

                  # Social Auth Management System
                  path('settings/', views.SettingsView.as_view(), name='settings'),
                  path('settings/password/', views.password, name='password'),
                  ######################################################################


                  # Rich Text Editor
                   path('summernote/', include('django_summernote.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
