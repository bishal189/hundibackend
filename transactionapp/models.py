from django.db import models
from authapp.models import Account
# Create your models here.

#for people working in company
class BankDetail(models.Model):
    companyWorker=models.ForeignKey(Account,on_delete=models.CASCADE)
    bankName=models.CharField(max_length=200)
    currencyCode=models.CharField(max_length=4)
    bankAccountNumber=models.CharField(max_length=50)
    created_at=models.DateField(auto_now_add=True)

#For sending Money
class Sender(models.Model):
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=50)
    email=models.EmailField()
    phoneNumber=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    city=models.CharField(max_length=40)
    address=models.CharField(max_length=40)
    bankName=models.CharField(max_length=100)
    currencyCode=models.CharField(max_length=4)
    created_at=models.DateField(auto_now_add=True)

#Information about Receiver
class Receiver(models.Model):
    fullName=models.CharField(max_length=50)
    bankName=models.CharField(max_length=100)
    bankAccountNumber=models.CharField(max_length=100)
    currencyCode=models.CharField(max_length=4)
    created_at=models.DateField(auto_now_add=True)

#For creating a relation between sender and receiver
class Transaction(models.Model):
    sender=models.ForeignKey(Sender,on_delete=models.CASCADE)
    receiver=models.ForeignKey(Receiver,on_delete=models.CASCADE)
    sentAmount=models.IntegerField()
    receivedAmount=models.IntegerField()
    status_choices=[
        ('RECEIVED','Received'),
        ('PAID','Paid'),
        ('CANCELLED','Cancelled'),
    ]
    status=models.CharField(choices=status_choices,max_length=15)
    created_at=models.DateField(auto_now_add=True)
    completed_at=models.DateField(auto_now_add=True)

