from django.db import models
from authapp.models import Account
# Create your models here.

#for people working in company
class BankDetail(models.Model):
    companyWorker=models.ForeignKey(Account,on_delete=models.CASCADE)
    bankName=models.CharField(max_length=200)
    currencyCode=models.CharField(max_length=4)
    bankAccountNumber=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)

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
    created_at=models.DateTimeField(auto_now_add=True)

#Information about Receiver
class Receiver(models.Model):
    fullName=models.CharField(max_length=50)
    bankName=models.CharField(max_length=100)
    bankAccountNumber=models.CharField(max_length=100)
    currencyCode=models.CharField(max_length=4)
    created_at=models.DateTimeField(auto_now_add=True)

#For creating a relation between sender and receiver
class TransferTransaction(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE,blank=True,null=True)
    sender=models.ForeignKey(Sender,on_delete=models.CASCADE)
    receiver=models.ForeignKey(Receiver,on_delete=models.CASCADE)
    sentAmount=models.DecimalField(max_digits=100,decimal_places=2)
    receivedAmount=models.DecimalField(max_digits=100,decimal_places=2)
    status_choices=[
        ('PROCESSING','Processing'),
        ('RECEIVED','Received'),
        ('PAID','Paid'),
        ('CANCELLED','Cancelled'),
    ]
    status=models.CharField(choices=status_choices,max_length=15,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    completed_at=models.DateField(blank=True,null=True)

#For creating a relation between sender and receiver
class PayTransaction(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE,blank=True,null=True)
    consumerName=models.CharField(max_length=100)
    consumerId=models.CharField(max_length=100,blank=True,null=True)
    companyName=models.CharField(max_length=100)
    type=models.CharField(max_length=100,blank=True,null=True)
    Amount=models.DecimalField(max_digits=100,decimal_places=2)
    status_choices=[
        ('PROCESSING','Processing'),
        ('RECEIVED','Received'),
        ('PAID','Paid'),
        ('CANCELLED','Cancelled'),
    ]
    status=models.CharField(choices=status_choices,max_length=15,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    completed_at=models.DateField(blank=True,null=True)


