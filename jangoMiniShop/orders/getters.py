from .models import Order


class OrderGetters(object):
    def __init__(self, request):
        self.user = request.user.id

    def get_user_orders(self):
        return Order.objects.filter(user=self.user)

    def get_orders_total(self):
        return sum(order.product.price * order.quantity for order in self.get_user_orders())
