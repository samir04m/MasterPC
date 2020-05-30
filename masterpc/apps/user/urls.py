from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),

    path('signup/', UserRegister.as_view(), name='signup'),
    path('register-success/', register_success, name='register_success'),
]
