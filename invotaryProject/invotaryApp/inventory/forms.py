from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'sku', 'price', 'quantity', 'supplier']
        labels = {
            'name': 'Item Name',
            'sku': 'Item SKU',
            'price': 'Item Price',
            'quantity': 'Item Quantity',
            'supplier': 'Item Supplier'
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Item Name'}),
            'sku': forms.TextInput(attrs={'placeholder': 'shirt-001'}),
            'price': forms.NumberInput(attrs={'placeholder': '9.99'}),
            'quantity': forms.NumberInput(attrs={'placeholder': '50'}),
            'supplier': forms.TextInput(attrs={'placeholder': 'Acme Corp'})
        }