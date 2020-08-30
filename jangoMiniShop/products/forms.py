from django import forms
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext as _
from .models import Product, Image

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "price"
        )

    preview_image = forms.FileField(
        widget=forms.ClearableFileInput(),
        label=_("Add preview image"),
        required=False,
    )

    image = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label=_("Add photos"),
        required=False,
    )

    def clean_photos(self):
        for upload in self.files.getlist("image"):
            validate_image_file_extension(upload)

    def save_photos(self, product):
        for upload in self.files.getlist("image"):
            photo = Image(product=product, image=upload)
            photo.save()


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
