from rest_framework import serializers
from .models import BuyTransaction,ProductItems,ProductType
from requestapp.serializers import AccountSerializer
class ProductItemsSerrializerForTransaction(serializers.ModelSerializer):
    class Meta:
        model=ProductItems
        fields=['item','unitPrice','status']
class BuyTransactionSerializer(serializers.ModelSerializer):
    buyer=AccountSerializer()
    item=ProductItemsSerrializerForTransaction()
    class Meta:
        model=BuyTransaction
        fields='__all__'

class ProductItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductItems
        fields='__all__'

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductType
        fields='__all__'