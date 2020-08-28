from django.contrib import admin
from .models import Product, Image
from .forms import ProductAdminForm


class ProductPhotoInline(admin.TabularInline):
    model = Image


@admin.register(Product)
class ShowAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    inlines = [ProductPhotoInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)
