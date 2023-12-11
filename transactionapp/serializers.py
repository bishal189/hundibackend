from rest_framework import serializers
from .models import BankDetail
from authapp.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name']  # Add other fields as needed

class BankDetailSerializer(serializers.ModelSerializer):
    companyWorker = AccountSerializer()  # Embed AccountSerializer for the related field

    class Meta:
        model = BankDetail
        fields = ['id', 'companyWorker', 'bankName', 'currencyCode', 'bankAccountNumber', 'created_at']
        read_only_fields = ['id', 'created_at']
