from rest_framework import serializers
from .models import Sender, Receiver, Transaction, Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name', 'email']  # Add other fields as needed

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
