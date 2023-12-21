from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.SendTransaction)
admin.site.register(models.WithdrawTransaction)
admin.site.register(models.TopUpTransaction)
