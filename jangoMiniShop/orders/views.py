from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from .forms import OrderCreate
from .getters import OrderGetters
from products.cart import Cart
from products.models import Product


def view_order(request):
    getters = OrderGetters(request)
    context = {
        'orders': getters.get_user_orders(),
        'orders_total': getters.get_orders_total()
    }
    return render(request, 'orders/orders.html', context)


def save_order(request):
    order = OrderCreate(request.POST)
    product = get_object_or_404(Product, id=request.POST['product'])
    cart = Cart(request)
    if order.is_valid():
        cart.remove(product)
        order.save()
    return redirect('view_order')


