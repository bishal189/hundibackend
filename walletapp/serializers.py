from rest_framework import serializers
from .models import TopUpTransaction,WithdrawTransaction,SendTransaction
from requestapp.serializers import AccountSerializer

class TopUpTransactionSerializer(serializers.ModelSerializer):
    user=AccountSerializer()
    class Meta:
        model=TopUpTransaction
        fields='__all__'

class WithDrawTransactionSerializer(serializers.ModelSerializer):
    user=AccountSerializer()
    class Meta:
        model=WithdrawTransaction
        fields='__all__'

class SendTransactionSerializer(serializers.ModelSerializer):
    user=AccountSerializer()
    class Meta:
        model=SendTransaction
        fields='__all__'