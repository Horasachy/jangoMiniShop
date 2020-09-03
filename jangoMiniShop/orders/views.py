from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderCreate
from .getters import OrderGetters


def view_order(request):
    getters = OrderGetters(request)
    context = {
        'orders': getters.get_user_orders(),
        'orders_total': getters.get_orders_total()
    }
    return render(request, 'orders/orders.html', context)


def save_order(request):
    order = OrderCreate(request.POST)
    if order.is_valid():
        order.save()
        return redirect('view_order')
