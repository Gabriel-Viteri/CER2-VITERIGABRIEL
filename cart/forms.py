from django import forms
from .models import ItemCarrito

class CartItemForm(forms.ModelForm):
    class Meta:
        model = ItemCarrito
        fields = ['cantidad', 'producto']
