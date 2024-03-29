from django.db import models
from authapp.models import Account
# Create your models here.


class RequestTransaction(models.Model):
    requester = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='request_transactions_made')
    requestedTo = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='request_transactions_received')
    requestedAmount=models.DecimalField(max_digits=10,decimal_places=2)
    statusChoices=[
        ('PENDING','Pending'),
        ('ACCEPT','Accept'),
        ('CANCELLED','Cancelled'),
    ]
    status=models.CharField(max_length=10,choices=statusChoices,default='PENDING')
    createdAt=models.DateTimeField(auto_now_add=True)
    completedAt=models.DateTimeField(null=True,blank=True)
    


