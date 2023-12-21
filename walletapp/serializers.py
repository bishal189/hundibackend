from rest_framework import serializers
from .models import TopUpTransaction
from requestapp.serializers import AccountSerializer

class TopUpTransactionSerializer(serializers.ModelSerializer):
    user=AccountSerializer()
    class Meta:
        model=TopUpTransaction
        fields='__all__'