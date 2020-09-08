from django.db.models import Q
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Builder(object):
    def __init__(self, request):
        self.search = request.GET.get('search', '')
        self.page = request.GET.get('page', 1)

    def get_filtered_products(self):

        products_list = Product.objects.filter(Q(name__icontains=self.search) | Q(description__icontains=self.search))
        paginator = Paginator(products_list, 1)

        products = paginator.page(self.page)

        return products
