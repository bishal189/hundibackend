from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .serializers import BankDetailSerializer,TransferTransactionSerializer,PayTransactionSerializer,SenderSerializer,ReceiverSerializer
from  .models import TransferTransaction,BankDetail,Sender,Receiver,PayTransaction
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
import json
from django.db.models import Sum

# Create your views here.

@csrf_exempt
@api_view(['POST'])
def CreateNewTransferTransaction(request):
    if request.method=="POST":
        data=json.loads(request.body)
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
        
        sender,created=Sender.objects.get_or_create(firstName=senderFirstName,lastName=senderLastName,email=senderEmail,phoneNumber=senderPhoneNumber,country=senderCountry,city=senderCity,address=senderAddress,bankName="ddmo",currencyCode=senderCurrencyCode)
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

        transaction=TransferTransaction.objects.create(user=user,sender=sender,receiver=receiver,sentAmount=sentAmount,receivedAmount=receivedAmount,status='PROCESSING')
        print("transaction completed")

        data={'message':"Transaction started"}
        return Response(data,status=status.HTTP_201_CREATED)
    else:
        data={'error':"Method Not allowed"}
        return Response(data,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
def VerifyTransferTransaction(request):
    try:
        #get current latest transaction from that sender

        transaction=TransferTransaction.objects.filter(user=request.user).order_by('-id')[0]
        serializer=TransferTransactionSerializer(transaction)
        data={'data':serializer.data}
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        data={'error':"TransferTransaction Couldnot be Verified"}
        return Response(data,status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET']) 
def CancelTransferTransaction(request):
    try:
        transaction=TransferTransaction.objects.filter(user=request.user).order_by('-id')[0]
        transaction.status='CANCELLED'
        transaction.save()

        data={"message":"Transfer Transaction Cancelled"}
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e: 
        print(e)
        data={"error":" Transction couldnot be cancelled"}
        return Response(data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def GetTransferTransactionUserHistory(request,limit=None):
    try:
        if (limit is not None):

            transaction=TransferTransaction.objects.filter(user=request.user).order_by('-id')[:limit]
        
        else:
            transaction=TransferTransaction.objects.filter(user=request.user).order_by('-id')

        serializer=TransferTransactionSerializer(transaction,many=True)
        data={'data':serializer.data}
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e: 
        print(e)
        data={'error':"Couldnot get any transaction"}
        return Response(data,status=status.HTTP_401_UNAUTHORIZED)

@csrf_exempt
@api_view(['GET']) 
def CancelPayTransaction(request):
    try:
        transaction=PayTransaction.objects.filter(user=request.user).order_by('-id')[0]
        transaction.status='CANCELLED'
        transaction.save()

        data={"message":"Transaction Cancelled"}
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e: 
        print(e)
        data={"error":" Transction couldnot be cancelled"}
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
        print(e)
        data={"error":"Got some Error"}
        return Response(data,status=status.HTTP_400_BAD_REQUEST)
    



csrf_exempt
@api_view(['POST'])
def CreateNewPayTransaction(request):
    if request.method=="POST":
        data=json.loads(request.body)
        consumerName=data['consumerName']
        consumerId=data['consumerId']
        companyName=data['companyName']
        mobileNumber=data['mobileNumber']
        amount=data['amount']
        type=data['type']
      
        user=request.user
        
        buy=PayTransaction.objects.create(user=user,consumerName=consumerName,consumerId=consumerId,companyName=companyName,type=type,Amount=amount,status="PROCESSING")
        data={'message':"Transaction started"}
        return Response(data,status=status.HTTP_201_CREATED)
    else:
        data={'error':"Method Not allowed"}
        return Response(data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def GetPayTransactionUserHistory(request,limit=None):
    try:
        if (limit is not None):
            transaction=PayTransaction.objects.filter(user=request.user).order_by('-id')[:limit]
        else:
            transaction=PayTransaction.objects.filter(user=request.user).order_by('-id')


        serializer=PayTransactionSerializer(transaction,many=True)
        data={'data':serializer.data}
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e: 
        print(e)
        data={'error':"Couldnot get any transaction"}
        return Response(data,status=status.HTTP_401_UNAUTHORIZED)

        
@api_view(['GET'])
def Dashboard(request):
    try:
        transferTransaction=TransferTransaction.objects.filter(user=request.user,status="PAID")
        payTransaction=PayTransaction.objects.filter(user=request.user,status="PAID")
        total_sent_transfer = transferTransaction.aggregate(total_sent=Sum('sentAmount'))['total_sent'] or 0
        print(total_sent_transfer)

# Calculate the total sent amount for pay transactions
        total_sent_pay = payTransaction.aggregate(total_sent=Sum('Amount'))['total_sent'] or 0

# Sum up the total sent amount from both types of transactions

        transfer0=transferTransaction[0].sender.currencyCode
        total_sent_money = total_sent_transfer + total_sent_pay
        sucessfullTransfer=transferTransaction.count()+payTransaction.count()    
        data={'totalSentMoney':total_sent_money,'currencyCode':transfer0,'sucessFullTransfer':sucessfullTransfer}
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error':"Transcation couldnot be found"},status=status.HTTP_400_BAD_REQUEST)


#For admin routes start
@api_view(['GET'])
def GetTransferTransactionAdminHistory(request):
    try:
        if request.user.is_admin:
            transaction=TransferTransaction.objects.all().order_by('-id')

            serializer=TransferTransactionSerializer(transaction,many=True)
            data={'data':serializer.data}
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response({'error':"User is not admin"},status=400)
    except Exception as e:
        print(e)
        data={'error':"Couldnot get any transaction"}
        return Response(data,status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def GetPayTransactionAdminHistory(request):
    try:

        if request.user.is_admin:
            transaction=PayTransaction.objects.all().order_by('-id')
            serializer=PayTransactionSerializer(transaction,many=True)
            data={'data':serializer.data}
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response({'error:':"user is not admin"},status=400)
    except Exception as e:
        print(e)
        data={'error':"Couldnot get any transaction"}
        return Response(data,status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def ApproveTransferTransactionAdmin(request,transactId):
    try:
        if request.user.is_admin:

            transaction=TransferTransaction.objects.get(id=transactId)
            transaction.status='PAID'
            transaction.completed_at=timezone.now()

            transaction.save()

            data={"message":"Transfer Transaction Approved"}
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response({'error':"Only admin can approve this"},status=403)
    except Exception as e:
        print(e)
        data={"error":" Transction couldnot be accepted"}
        return Response(data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def DenyTransferTransactionAdmin(request,transactId):
    try:
        if request.user.is_admin:
            transaction=TransferTransaction.objects.get(id=transactId)
            transaction.status='CANCELLED'
            transaction.completed_at=timezone.now()
            transaction.save()



            data={"message":"Transfer Transaction Cancelled"}
        else:
            data={"error":"Only admin can cancel this"}
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        data={"error":" Transction couldnot be cancelled"}
        return Response(data,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def ApprovePayTransactionAdmin(request,transactId):
    try:
        if request.user.is_admin:

            transaction=PayTransaction.objects.get(id=transactId)
            transaction.status='PAID'
            transaction.save()

            data={"message":"Pay Transaction Approved"}
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response({'error':"Only admin can approve this"},status=403)
    except Exception as e:
        print(e)
        data={"error":" Pay couldnot be accepted"}
        return Response(data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def DenyPayTransactionAdmin(request,transactId):
    try:
        if request.user.is_admin:
            transaction=PayTransaction.objects.get(id=transactId)
            transaction.status='CANCELLED'
            transaction.save()

            data={"message":"Pay Transaction Cancelled"}
        else:
            data={"error":"Only admin can cancel this"}
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        data={"error":" Transaction couldnot be cancelled"}
        return Response(data,status=status.HTTP_400_BAD_REQUEST)

