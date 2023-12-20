from rest_framework import serializers
from .models import BuyTransaction,ProductItems
from requestapp.serializers import AccountSerializer
class ProductItemsSerrializer(serializers.ModelSerializer):
    class Meta:
        model=ProductItems
        fields=['item','unitPrice','status']
class BuyTransactionSerializer(serializers.ModelSerializer):
    buyer=AccountSerializer()
    item=ProductItemsSerrializer()
    class Meta:
        model=BuyTransaction
        fields='__all__'