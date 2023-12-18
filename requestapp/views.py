from django.shortcuts import render
from rest_framework.decorators import api_view
import json
from rest_framework import status
from rest_framework.response import Response
from authapp.models import Account
from .models import RequestTransaction
from .serializers import RequestTransactionSerializer
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
            responseData={'data':serializer.data}
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
            requestTransaction=RequestTransaction.objects.filter(requester=request.user).order_by('-id')
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
            transaction=RequestTransaction.objects.get(id=transactId,requestedTo=request.user)
            if transaction.status=='Accept':
                return Response({'error':"You cannot Accept this again..Already Accepted if You didnot received money contact support"})
            requester=transaction.requester
            requestedTo=request.user
            if requestedTo.balance<transaction.requestedAmount:
                return Response({'error':"You donot have enough funds to accept this request"})
            
            requester.balance=requester.balance+transaction.requestedAmount
            requestedTo.balance=requestedTo.balance-transaction.requestedAmount
            requestedTo.save()
            requester.save()
            transaction.status='Accept'
            transaction.save()

            return Response({"message":"You have Sucessfully Accepted the Request"},status=status.HTTP_200_OK)


        

            
    except Exception as e:
        error=str(e)
        return Response({'error':f"Some Unexpected Error Occured ... {error}"},status=status.HTTP_400_BAD_REQUEST)