from .models import Account
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .serializers import BankDetailSerializer
from  .models import Transaction,BankDetail,Sender,Receiver
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@csrf_exempt
@api_view(['POST'])
def CreateNewTransaction(request):
    if request.method=="POST":
        senderFirstName=request.POST['senderFirstName']
        senderLastName=request.POST['senderLastName']
        senderEmail=request.POST['senderEmail']
        senderPhoneNumber=request.POST['senderPhoneNumber']
        senderCountry=request.POST['senderCountry']
        senderCity=request.POST['senderCity']
        senderAddress=request.POST['senderAddress']
        senderBankName=request.POST['senderBankName']
        senderCurrencyCode=request.POST['senderCurrencyCode']
        
        sender,created=Sender.objects.get_or_create(firstName=senderFirstName,lastName=senderLastName,email=senderEmail,phoneNumber=senderPhoneNumber,country=senderCountry,city=senderCity,address=senderAddress,bankName=senderBankName,currencyCode=senderCurrencyCode)
        print("sender created",created)

        receiverFullName=request.POST['receiverFullName']
        receiverBankName=request.POST['receiverBankName']
        receiverCurrencyCode=request.POST['receiverCurrencyCode']
        receiverBankAccountNumber=request.POST['receiverBankAccountNumber']

        receiver,created=Receiver.objects.get_or_create(fullName=receiverFullName,bankName=receiverBankName,bankAccountNumber=receiverBankAccountNumber,currencyCode=receiverCurrencyCode)
        print("receiver created",created)

        sentAmount=request.POST['sentAmount']
        receivedAmount=request.POST['receivedAmount']

        transaction=Transaction.objects.create(sender=sender,receiver=receiver,sentAmount=sentAmount,receivedAmount=receivedAmount)
        print("transaction completed")

        data={'message':"Transaction started"}
        return Response(data,status=status.HTTP_201_CREATED)
    else:
        data={'error':"Method Not allowed"}
        return Response(data,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET']) 
def CancelTransaction(request):
    transaction=Transaction.objects.get(request.user)
    transaction.cancelled=False
    transaction.save()

    data={"message":"Transaction Cancelled"}
    return Response(data,status=status.HTTP_200_OK)


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
    



