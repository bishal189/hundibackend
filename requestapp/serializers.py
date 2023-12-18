from rest_framework import serializers
from .models import * 
from authapp.models import Account
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=['id','name']


class RequestTransactionSerializer(serializers.ModelSerializer):
    requester=AccountSerializer()
    requestedTo=AccountSerializer()
    class Meta:
        model=RequestTransaction
        fields='__all__'