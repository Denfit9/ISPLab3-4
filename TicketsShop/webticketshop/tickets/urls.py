from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.tickets_list, name='ticket_list'),
    path('add-ticket/', views.create, name='ticket_insert'),
    path('delete-ticket/<int:id>/', views.delete, name='ticket_delete'),
    path('add-ticket/<int:id>/', views.create, name='ticket_update')
]