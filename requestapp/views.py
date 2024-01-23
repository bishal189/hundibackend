from django.shortcuts import render
from rest_framework.decorators import api_view
import json
from rest_framework import status
from rest_framework.response import Response
from authapp.models import Account
from .models import RequestTransaction
from .serializers import RequestTransactionSerializer
from django.utils import timezone
# Create your views here.

@api_view(['POST'])
def createNewRequest(request):
    try:
        if request.method=='POST':
            data=json.loads(request.body)
            requester=request.user
            requestedTo=Account.objects.get(id=data['requestedTo'])
            requestedAmount=data['requestedAmount']
            newRequest=RequestTransaction.objects.create(requester=requester,requestedTo=requestedTo,requestedAmount=requestedAmount)
            serializer=RequestTransactionSerializer(newRequest)
            responseData={'message':"Request Sent Sucessfully . You will receive an email once your request is Accepted by your Requested person"}
            return Response(responseData,status=status.HTTP_200_OK)

        else:
            return Response({'error':"Method Not Allowed.Only Post allowed in this endponit"},status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        error=str(e)
        return Response({'error':f"Some Unexpected Error Occured...{error}"},status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def GetAllRequestTransaction(request):
    try:
        if request.method=="GET":

            if request.user.is_admin:

                requestTransaction=RequestTransaction.objects.all().order_by('-id')
            else:
                requestTransaction=RequestTransaction.objects.filter(requestedTo=request.user,status='PENDING').order_by('-id')
            serializer=RequestTransactionSerializer(requestTransaction,many=True)
            dataResponse={'data':serializer.data}
            return Response(dataResponse,status=status.HTTP_200_OK)
        else:
            return Response({'error':"Method Not Allowed"},status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        error=str(e)
        return Response({'error':f"Some Unexpected Error Occured...{error}"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def AcceptRequestTransaction(request,transactId):
    try:
        if request.method=="GET":
            if request.user.is_admin:

                transaction=RequestTransaction.objects.get(id=transactId)
            else:
                transaction=RequestTransaction.objects.get(id=transactId,requestedTo=request.user)

            if transaction.status!='PENDING':
                return Response({'error':"You cannot Accept this ..Already Accepted or denied Contact Support if you didnot receive money but it is accepted "},status=status.HTTP_403_FORBIDDEN)
            requester=transaction.requester
            requestedTo=request.user
            if requestedTo.balance<transaction.requestedAmount:
                return Response({'error':"You donot have enough funds to accept this request"},status=status.HTTP_403_FORBIDDEN)
            
            requester.balance=requester.balance+transaction.requestedAmount
            requestedTo.balance=requestedTo.balance-transaction.requestedAmount
            requestedTo.save()
            requester.save()
            transaction.status='ACCEPT'
            transaction.completedAt=timezone.now()
            transaction.save()

            return Response({"message":"You have Sucessfully Accepted the Request"},status=status.HTTP_200_OK)
            
    except Exception as e:
        error=str(e)
        return Response({'error':f"Some Unexpected Error Occured ... {error}"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def DenyRequestTransaction(request,transactId):
    try:
        if request.method=="GET":
            if request.user.is_admin:
                transaction=RequestTransaction.objects.get(id=transactId)
            else:
                transaction=RequestTransaction.objects.get(id=transactId,requestedTo=request.user)
            if transaction.status!='PENDING':
                return Response({'error':"You cannot deny this ..Already denied or accepted.Contact Support if you didnot receive money but it is accepted "},status=status.HTTP_400_BAD_REQUEST)
            transaction.status='CANCELLED'
            transaction.completedAt=timezone.now()
            transaction.save()

            return Response({"message":"You have Sucessfully Denied the Request"},status=status.HTTP_200_OK)
            
    except Exception as e:
        error=str(e)
        return Response({'error':f"Some Unexpected Error Occured ... {error}"},status=status.HTTP_400_BAD_REQUEST)

