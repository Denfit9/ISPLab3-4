from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView,PasswordResetConfirmView

urlpatterns = [
    path('tickets/', include('tickets.urls')),
    path('', views.home),
    path('login/', LoginView.as_view(
        template_name='main/login.html'
    )),
    path('logout/', LogoutView.as_view(
        template_name='main/logout.html'
    )),
    path('register/', views.register, name='register'),
    path('change-password/', views.change_password, name='change_password'),
    path('reset-password/', PasswordResetView.as_view(), name='reset_password'),
    path('reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
]
