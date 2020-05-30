from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.user.urls')),
    
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logout_then_login, name='logout'),
]
