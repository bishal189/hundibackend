from django.db import models
from authapp.models import Account
# Create your models here.

class TopUpTransaction(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    bankAccountNumber=models.CharField(max_length=50)
    name=models.CharField(max_length=50,null=True,blank=True)   
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    statusChoices=[
        ('PENDING','Pending'),
        ('ACCEPT','Accept'),
        ('CANCEL','Cancel'),

    ]

    status=models.CharField(max_length=10,default='PENDING',choices=statusChoices)
    createdAt=models.DateTimeField(auto_now_add=True)
    completedAt=models.DateTimeField(null=True,blank=True)

class WithdrawTransaction(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    bankAccountNumber=models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    statusChoices=[
        ('PENDING','Pending'),
        ('ACCEPT','Accept'),
        ('CANCEL','Cancel'),
    ]

    status=models.CharField(max_length=10,default='PENDING',choices=statusChoices)
    createdAt=models.DateTimeField(auto_now_add=True)
    completedAt=models.DateTimeField(null=True,blank=True)

class SendTransaction(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    bankAccountNumber=models.CharField(max_length=100,blank=True,null=True)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    statusChoices=[
        ('PENDING','Pending'),
        ('ACCEPT','Accept'),
        ('CANCEL','Cancel'),
    ]
    status=models.CharField(max_length=10,default='PENDING',choices=statusChoices)
    createdAt=models.DateTimeField(auto_now_add=True)
    completedAt=models.DateTimeField(null=True,blank=True)

