from rest_framework import serializers
from .models import *
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



class SenderSerializer(serializers.ModelSerializer):
    user = AccountSerializer()

    class Meta:
        model = Sender
        fields = ['id', 'user', 'firstName', 'lastName', 'email', 'phoneNumber', 'country', 'city', 'address', 'bankName', 'currencyCode', 'created_at']
        read_only_fields = ['id', 'created_at']

class ReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receiver
        fields = ['id', 'fullName', 'bankName', 'bankAccountNumber', 'currencyCode', 'created_at']
        read_only_fields = ['id', 'created_at']

class TransactionSerializer(serializers.ModelSerializer):
    sender = SenderSerializer()
    receiver = ReceiverSerializer()

    class Meta:
        model = Transaction
        fields = ['id', 'sender', 'receiver', 'sentAmount', 'receivedAmount', 'status', 'created_at', 'completed_at']
        read_only_fields=['id','created_at']