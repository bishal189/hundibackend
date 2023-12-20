from django import  forms
from .models import ProductItems,ProductType,BuyTransaction

class ProductItemForm(forms.ModelForm):
    class Meta:
        model=ProductItems
        fields='__all__'