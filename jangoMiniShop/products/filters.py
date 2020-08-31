from django.db.models import Q
from .models import Product


class Builder(object):
    def __init__(self, request):
        self.search = request.GET.get('search', '')

    def get_filtered_products(self):
        return Product.objects.filter(Q(name__icontains=self.search) | Q(description__icontains=self.search))