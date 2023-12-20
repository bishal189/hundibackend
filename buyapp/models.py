from django.db import models
from authapp.models import Account
# Create your models here.
class ProductItems(models.Model):
    item=models.CharField(max_length=100)
    image=models.ImageField(upload_to='productImages/')
    alt=models.CharField(max_length=100)
    unitPrice=models.DecimalField(max_digits=10,decimal_places=2)
    statusChoices=[
        ('PENDING','Pending'),
        ('ACCEPT','ACCEPT'),
    ]
    status=models.CharField(max_length=20,choices=statusChoices,default="PENDING")
class ProductType(models.Model):
    productType=models.CharField(max_length=100)
    products=models.ManyToManyField(ProductItems)
    createdAt=models.DateField(auto_now_add=True)

class BuyTransaction(models.Model):
    buyer=models.ForeignKey(Account,on_delete=models.CASCADE)
    item=models.ForeignKey(ProductItems,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    statusChoices=[
        ('PROCESSING','Processing'),
        ('PAID','Paid'),
        ('CANCELLED','Cancelled'),
        ]
    status=models.CharField(max_length=100,choices=statusChoices,default="PROCESSING")
    totalPrice=models.DecimalField(max_digits=10,decimal_places=2)
    createdAt=models.DateTimeField(auto_now_add=True)
    completedAt=models.DateTimeField(blank=True,null=True)

