from django import forms
from .models import Client, Product, Order, Stock
from django import forms
from .models import SpecialOffer
from django import forms
from .models import Promotion

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

class SpecialOfferForm(forms.ModelForm):
    class Meta:
        model = SpecialOffer
        fields = "__all__"


class PromotionForm(forms.ModelForm):

    class Meta:
        model = Promotion
        fields = [
            'promotion_name',
            'discount_type',
            'discount_value',
            'applicable_products',
            'start_date',
            'end_date',
            'minimum_order_value',
            'priority'
        ]

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'applicable_products': forms.SelectMultiple(attrs={'size': 8}),
        }

from django import forms
from .models import LoyaltyMembership, LoyaltyReward

class LoyaltyMembershipForm(forms.ModelForm):
    class Meta:
        model = LoyaltyMembership
        fields = '__all__'

class LoyaltyRewardForm(forms.ModelForm):
    class Meta:
        model = LoyaltyReward
        fields = '__all__'
