from django.contrib import admin
from .models import * 
# Register your models here.
admin.site.register(Sender)
admin.site.register(Receiver)
admin.site.register(BankDetail)
admin.site.register(TransferTransaction)
admin.site.register(PayTransaction)