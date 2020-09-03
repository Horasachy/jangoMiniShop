from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('order/save', views.save_order, name='order_save'),
    path('orders', views.view_order, name='view_order'),
]
