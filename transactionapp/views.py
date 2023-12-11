from .models import Account
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .serializers import BankDetailSerializer,TransactionSerializer,SenderSerializer,ReceiverSerializer
from  .models import Transaction,BankDetail,Sender,Receiver
from rest_framework.response import Response
from rest_framework import status
import json
# Create your views here.

@csrf_exempt
@api_view(['POST'])
def CreateNewTransaction(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
        sender=data['sender']
        senderFirstName=sender['senderFirstName']
        senderLastName=sender['senderLastName']
        senderEmail=sender['senderEmail']
        senderPhoneNumber=sender['senderPhoneNumber']
        senderCountry=sender['senderCountry']
        senderCity=sender['senderCity']
        senderAddress=sender['senderAddress']
        # senderBankName=sender['senderBankName']
        senderCurrencyCode=sender['senderCurrencyCode']

        user=request.user
        print(user)
        
        sender,created=Sender.objects.get_or_create(user=user,firstName=senderFirstName,lastName=senderLastName,email=senderEmail,phoneNumber=senderPhoneNumber,country=senderCountry,city=senderCity,address=senderAddress,bankName="ddmo",currencyCode=senderCurrencyCode)
        print("sender created",created)
        receiver=data['receiver']
        receiverFullName=receiver['receiverFullName']
        receiverBankName=receiver['receiverBankName']
        receiverCurrencyCode=receiver['receiverCurrencyCode']
        receiverBankAccountNumber=receiver['receiverBankAccountNumber']

        receiver,created=Receiver.objects.get_or_create(fullName=receiverFullName,bankName=receiverBankName,bankAccountNumber=receiverBankAccountNumber,currencyCode=receiverCurrencyCode)
        print("receiver created",created)

        sentAmount=data['sentAmount']
        receivedAmount=data['receivedAmount']

        transaction=Transaction.objects.create(sender=sender,receiver=receiver,sentAmount=sentAmount,receivedAmount=receivedAmount,status='PROCESSING')
        print("transaction completed")

        data={'message':"Transaction started"}
        return Response(data,status=status.HTTP_201_CREATED)
    else:
        data={'error':"Method Not allowed"}
        return Response(data,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
def VerifyTransaction(request):
    try:
        requestUser=request.user
        #get current latest transaction from that sender
        sender=Sender.objects.filter(requestUser).order_by('-id')[0]

        transaction=Transaction.objects.filter(sender).order_by('-id')[0]
        serializer=TransactionSerializer(transaction)
        data={'data':serializer.data}
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        data={'error':"Transaction Couldnot be Verified"+e}
        return Response(data,status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET']) 
def CancelTransaction(request):
    try:
        transaction=Transaction.objects.get(request.user)
        transaction.cancelled=False
        transaction.save()

        data={"message":"Transaction Cancelled"}
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e: 
        data={"error":" Transction couldnot be cancelled"+e}
        return Response(data,status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET'])
def GetBankCards(request,countryCode):
    try:
        banks=BankDetail.objects.filter(currencyCode=countryCode)  
        serializer = BankDetailSerializer(banks, many=True)
        data={'data':serializer.data}
        return Response(data,status=status.HTTP_200_OK)

    except Exception as e: 
        data={"error":"Got some Error"+e}
        return Response(data,status=status.HTTP_400_BAD_REQUEST)
    



