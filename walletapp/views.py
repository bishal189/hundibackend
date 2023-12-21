from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from django.utils import timezone
from .models import TopUpTransaction,WithdrawTransaction,SendTransaction
from .serializers import TopUpTransactionSerializer,WithDrawTransactionSerializer,SendTransactionSerializer
# Create your views here.
@api_view(['POST'])
def CreateNewTopUpTransaction(request):
    try:
        data=json.loads(request.body)
        bankAccountNumber=data['bankAccountNumber']
        amount=data['amount']
        TopUpTransaction.objects.create(user=request.user,bankAccountNumber=bankAccountNumber,amount=amount)
        return Response({'message':'Transaction Created Successfully'},status=status.HTTP_201_CREATED)
    
    except Exception as e : 
        error=str(e)
        return Response({'error':f"Unexpected Error occured {error}"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def AcceptTopUpTransaction(request,transactionId):
    try:
        if request.user.is_admin!=True:
            return Response({'error':"only Admin can accept a topup"},status=status.HTTP_401_UNAUTHORIZED)
        transaction=TopUpTransaction.objects.get(id=transactionId)
        if transaction.status=='ACCEPT':
            return Response({'error':"Transaction is already accepted cannot accept again"},status=status.HTTP_403_FORBIDDEN)
        user=request.user
        user.balance=transaction.amount+user.balance
        user.save()

        transaction.status='ACCEPT'
        transaction.completedAt=timezone.now()
        transaction.save()
        return Response({'message':"Transaction Successfully approved"},status=status.HTTP_200_OK)

    except Exception as e:
        error=str(e)
        return Response({'error':f"Unexpected error occured {error}"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def GetTopUpTransactionHistory(request):
    try:
        transactions=TopUpTransaction.objects.filter(user=request.user).order_by('-id')
        serializer=TopUpTransactionSerializer(transactions,many=True)
        data={'data':serializer.data}
        return Response(data,status=status.HTTP_200_OK)
    
    except Exception as e:
        error=str(e)
        return Response({'error':f"Unexpected Error occured {error}"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def CreateNewWithDrawTransaction(request):
    try:
        data=json.loads(request.body)
        bankAccountNumber=data['bankAccountNumber']
        amount=data['amount']
        WithdrawTransaction.objects.create(user=request.user,bankAccountNumber=bankAccountNumber,amount=amount)
        return Response({'message':'Transaction Created Successfully'},status=status.HTTP_201_CREATED)
    
    except Exception as e : 
        error=str(e)
        return Response({'error':f"Unexpected Error occured {error}"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def AcceptWithDrawTransaction(request,transactionId):
    try:
        if request.user.is_admin!=True:
            return Response({'error':"only Admin can accept a withdraw"},status=status.HTTP_401_UNAUTHORIZED)
        transaction=WithdrawTransaction.objects.get(id=transactionId)
        if transaction.status=='ACCEPT':
            return Response({'error':"Transaction is already accepted cannot accept again"},status=status.HTTP_403_FORBIDDEN)
        user=request.user
        user.balance=user.balance-transaction.amount
        if user.balance<0:
            return Response({'error':"U donot have enough funds for this withdraw"})
        
        user.save()

        transaction.status='ACCEPT'
        transaction.completedAt=timezone.now()
        transaction.save()
        return Response({'message':"Transaction Successfully approved"},status=status.HTTP_200_OK)

    except Exception as e:
        error=str(e)
        return Response({'error':f"Unexpected error occured {error}"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def GetWithDrawTransactionHistory(request):
    try:
        transactions=WithdrawTransaction.objects.filter(user=request.user).order_by('-id')
        serializer=WithDrawTransactionSerializer(transactions,many=True)
        data={'data':serializer.data}
        return Response(data,status=status.HTTP_200_OK)
    
    except Exception as e:
        error=str(e)
        return Response({'error':f"Unexpected Error occured {error}"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def CreateNewSendTransaction(request):
    try:
        data=json.loads(request.body)
        recipentName=data['recipentName']
        amount=data['amount']
        SendTransaction.objects.create(user=request.user,recipentName=recipentName,amount=amount)
        return Response({'message':'Transaction Created Successfully'},status=status.HTTP_201_CREATED)
    
    except Exception as e : 
        error=str(e)
        return Response({'error':f"Unexpected Error occured {error}"},status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def AcceptSendTransaction(request,transactionId):
    try:
        if request.user.is_admin!=True:
            return Response({'error':"only Admin can accept a sebd trabsactub"},status=status.HTTP_401_UNAUTHORIZED)
        transaction=SendTransaction.objects.get(id=transactionId)
        if transaction.status=='ACCEPT':
            return Response({'error':"Transaction is already accepted cannot accept again"},status=status.HTTP_403_FORBIDDEN)
        user=request.user
        user.balance=user.balance-transaction.amount
        if user.balance<0:
            return Response({'error':"U donot have enough funds for this Send Operatoin"})
        
        user.save()

        transaction.status='ACCEPT'
        transaction.completedAt=timezone.now()
        transaction.save()
        return Response({'message':"Transaction Successfully approved"},status=status.HTTP_200_OK)

    except Exception as e:
        error=str(e)
        return Response({'error':f"Unexpected error occured {error}"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def GetSendTransactionHistory(request):
    try:
        transactions=SendTransaction.objects.filter(user=request.user).order_by('-id')
        serializer=SendTransactionSerializer(transactions,many=True)
        data={'data':serializer.data}
        return Response(data,status=status.HTTP_200_OK)
    
    except Exception as e:
        error=str(e)
        return Response({'error':f"Unexpected Error occured {error}"},status=status.HTTP_400_BAD_REQUEST)


