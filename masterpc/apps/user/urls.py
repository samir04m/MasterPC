from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('pc/create/', CreatePc.as_view(), name='create_pc'),
    path('pc/<int:pk>/', UpdatePc.as_view(), name='update_pc'),
    path('pc/<int:pk>/delete/', DeletePc.as_view(), name='delete_pc'),

    path('signup/', UserRegister.as_view(), name='signup'),
    path('register-success/', register_success, name='register_success'),
]
