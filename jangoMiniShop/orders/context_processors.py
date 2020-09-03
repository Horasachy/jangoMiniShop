from .models import Order


def orders(request):
    return {'orders':  Order.objects.filter(user=request.user.id)}
