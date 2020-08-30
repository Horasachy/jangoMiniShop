from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .cart import Cart
from .models import Product
from .forms import CartAddProductForm


@login_required(login_url='login')
def index(request):
    cart_product_form = CartAddProductForm()
    context = {'products': Product.objects.all(), 'cart_product_form': cart_product_form}

    return render(request, 'products/index.html', context)


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):

    cart = Cart(request)
    print(cart)
    return render(request, 'products/detail.html', {'cart': cart})
