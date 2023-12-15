from rest_framework import serializers
from .models import *
from authapp.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ['password']  # Exclude the 'email' field

class BankDetailSerializer(serializers.ModelSerializer):
    companyWorker = AccountSerializer()  # Embed AccountSerializer for the related field

    class Meta:
        model = BankDetail
        fields = ['id', 'companyWorker', 'bankName', 'currencyCode', 'bankAccountNumber', 'created_at']
        read_only_fields = ['id', 'created_at']



class SenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sender
        fields = ['id', 'firstName', 'lastName', 'email', 'phoneNumber', 'country', 'city', 'address', 'bankName', 'currencyCode', 'created_at']
        read_only_fields = ['id', 'created_at']

class ReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receiver
        fields = ['id', 'fullName', 'bankName', 'bankAccountNumber', 'currencyCode', 'created_at']
        read_only_fields = ['id', 'created_at']

class TransferTransactionSerializer(serializers.ModelSerializer):
    sender = SenderSerializer()
    receiver = ReceiverSerializer()
    user = AccountSerializer()


    class Meta:
        model = TransferTransaction
        fields = ['id','user', 'sender', 'receiver', 'sentAmount', 'receivedAmount', 'status', 'created_at', 'completed_at']
        read_only_fields=['id','created_at']


class PayTransactionSerializer(serializers.ModelSerializer):
    user = AccountSerializer()


    class Meta:
        model = PayTransaction
        fields = '__all__'
