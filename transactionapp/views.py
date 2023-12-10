from .models import Account
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from django.contrib import  auth
from  .models import Transaction,BankDetail,Sender,Receiver
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


def CreateNewTransaction(request):
