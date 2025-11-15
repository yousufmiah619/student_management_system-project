from django.urls import path
from .views import *

urlpatterns = [
    path('register/',register_user),
    path('login/',login),
    path('otp/create/',create_otp),
    path('otp/verify/',verify_otp),
    path('password-reset/request/',request_password_reset),
    path('password-reset/confirm/',reset_password),
    path('password-change/',change_password),
]
