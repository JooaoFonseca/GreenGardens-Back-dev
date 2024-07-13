from django import forms
from .models import descricao
from django_svg_image_form_field import SvgAndImageFormField

class descricaoForm(forms.ModelForm):
    class Meta:
        model = descricao
        exclude = []
        field_images = {
            'image': SvgAndImageFormField,
        }