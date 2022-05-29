"""webticketshop URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_redirect, name='login_redirect'),
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
]
