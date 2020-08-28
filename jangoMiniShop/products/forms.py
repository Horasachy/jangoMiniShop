from django import forms
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext as _

from .models import Product, Image


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "name",
            "description",
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
