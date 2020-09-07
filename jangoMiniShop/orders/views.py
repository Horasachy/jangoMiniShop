from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .models import Order
from .forms import OrderCreate
from .getters import OrderGetters
from products.cart import Cart
from products.models import Product



@login_required(login_url='login')
def view_order(request):
    getters = OrderGetters(request)
    context = {
        'orders': getters.get_user_orders(),
        'orders_total': getters.get_orders_total()
    }
    return render(request, 'orders/orders.html', context)


@login_required(login_url='login')
def save_order(request):
    order = OrderCreate(request.POST)
    product = get_object_or_404(Product, id=request.POST['product'])
    cart = Cart(request)
    if order.is_valid():
        cart.remove(product)
        order.save()
    return redirect('view_order')


@login_required(login_url='login')
@csrf_exempt
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return JsonResponse({}, status=204)

