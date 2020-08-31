from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('products', views.index, name='products'),
    url(r'^card/$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
    url(r'^product/(?P<product_id>\d+)/$', views.product, name='product')
]

