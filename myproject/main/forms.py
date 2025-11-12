from django import forms
from .models import Client, Product, Order, Stock

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'address']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'product', 'quantity']


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product', 'quantity']
