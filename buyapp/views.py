from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import json
from django.utils import timezone
from .models import ProductType,ProductItems,BuyTransaction
from .forms import ProductItemForm
from .serializers import BuyTransactionSerializer,ProductItemsSerializer,ProductTypeSerializer
# Create your views here.

@api_view(['POST'])
def CreateNewProductItem(request):
    try:
        if  request.user.is_admin!=True:
            return Response({'error':"Only admin has acess to add new item"})
        formData=ProductItemForm(request.POST,request.FILES)
        if formData.is_valid():
            formData.save()
            return Response({'message':"Item has been sucessfully Added"})
        else:
            print(formData.errors)
            return Response({'error':"Incoming Data not correct"},status=status.HTTP_403_FORBIDDEN)
    except Exception as e: 
        error=str(e)
        return Response({'error':f"Unexpected Error Occured...{error}"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def CreateNewProductType(request):
    try:
        if  request.user.is_admin!=True:
            return Response({'error':"Only Admin can add new product Type"})
    
        data=json.loads(request.body)
        producttype=data['producttype']
        product,created=ProductType.objects.get_or_create(producttype=producttype)
        if created:
            return Response({'message':"Product Type has been added sucessfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({"error":"Cannot Create same Type again"},status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:    
        error=str(e)
        return Response({'error':f"UNexpected error Occured {error}"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def AddProductItemToProductType(request,productTypeId,productItemId):
    try:
        if  request.user.is_admin!=True:
            return Response({'error':"Only Admin can add new product Type"})
        productType=ProductType.objects.get(id=productTypeId)
        productItem=ProductItems.objects.get(id=productItemId)
        # if productItem.status=="ACCEPT":
        #     return Respone({'error':"This Product Item has been accepted Somewhere else"})
        productType.products.add(productItem)
        productItem.status='ACCEPT'
        productItem.save()
        productType.save()

        return Response({'message':"Product  has been added to Product Typesucessfully"},status=status.HTTP_200_OK)

    except Exception as e:    
        error=str(e)
        return Response({'error':f"UNexpected error Occured {error}"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def ListProductItem(request,productTypeId):
    try:
        productType=ProductType.objects.get(id=productTypeId)
        productItems=productType.products.all()
        serializer=ProductItemsSerializer(productItems,many=True)
        data={'data':serializer.data}
        return Response(data,status=status.HTTP_200_OK)
    
    except Exception as e: 
        error=str(e)
        return Response({'error':f"Unexpected Error Occured{error}"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def ListProductType(request):
    try:
        productType=ProductType.objects.all().order_by('-id')
        print(productType)
        serializer=ProductTypeSerializer(productType,many=True)
        data={'data':serializer.data}
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e: 
        error=str(e)
        return Response({'error':f"Unexpected error occured {error}"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def ShowProductItemDetail(request,productItemId):
    try:
        productItem=ProductItems.objects.get(id=productItemId)
        serializer=ProductItemsSerializer(productItem)
        data={'data':serializer.data}
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e: 
        error=str(e)
        return Response({'error':f"Unexpected Error occured..{error}"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def CreateNewBuyTransaction(request):
    try:
        data=json.loads(request.body)
        productItemId=data['productItemId']
        productItem=ProductItems.objects.get(id=productItemId)
        if productItem.status=='PENDING':
            return Response({'error':"Cannot add this product which is not accepted"},status=status.HTTP_403_FORBIDDEN)

        BuyTransaction.objects.create(buyer=request.user,item=productItem,quantity=data['quantity'],totalPrice=data['totalPrice'])
        return Response({'message':"New Buy Transaction Created Successfully"},status=status.HTTP_201_CREATED)

    except Exception as e:    
        error=str(e)
        return Response({'error':f"UNexpected error Occured {error}"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetBuyTransactionHistory(request,limit=None):
    try:

        transaction=BuyTransaction.objects.filter(buyer=request.user).order_by('-id')
        if limit is not None:
            transaction=transaction[:limit]
        serializer=BuyTransactionSerializer(transaction,many=True)
        data={'data':serializer.data}
        return Response(data,status=status.HTTP_200_OK)

    except Exception as e:    
        error=str(e)
        return Response({'error':f"UNexpected error Occured {error}"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET']) 
def CancelBuyTransaction(request):
    try:
        transaction=BuyTransaction.objects.filter(buyer=request.user).order_by('-id')[0]
        transaction.status='CANCELLED'
        transaction.save()
        data={"message":"Buy Transaction Cancelled"}
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e: 
        error=str(e)
        data={"error":f"Transction couldnot be cancelled{error}"}
        return Response(data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def ApproveBuyTransaction(request,transactId):
    try:
        if request.user is None:
            return Response({'error':"ONLy admin can approve a buy transaction"},status=status.HTTP_401_UNAUTHORIZED)
   
        if request.user.is_admin!=True:
            return Response({'error':"ONLy admin can approve a buy transaction"},status=status.HTTP_401_UNAUTHORIZED)
        transaction=BuyTransaction.objects.get(id=transactId)
        transaction.status='PAID'
        transaction.completedAt=timezone.now()
        transaction.save()
        serializer=BuyTransactionSerializer(transaction)
        data={'data':serializer.data}
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e: 
        error=str(e)
        data={"error":f"Some unexpected Error {error}"}

@api_view(['GET'])
def DenyBuyTransaction(request,transactId):
    try:
        if request.user is None:
            return Response({'error':"ONLy admin can approve a buy transaction"},status=status.HTTP_401_UNAUTHORIZED)

        if request.user.is_admin!=True:
            return Response({'error':"ONLy admin can approve a buy transaction"},status=status.HTTP_401_UNAUTHORIZED)
        transaction=BuyTransaction.objects.get(id=transactId)
        transaction.status='CANCELLED'
        transaction.completedAt=timezone.now()
        transaction.save()
        serializer=BuyTransactionSerializer(transaction)
        data={'data':serializer.data}
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        error=str(e)
        data={"error":f"Some unexpected Error {error}"}



@api_view(['GET'])
def GetBuyTransactionAdminHistory(request):
    try:
        if request.user.is_admin:
            transaction=BuyTransaction.objects.filter(status='PROCESSING').order_by('-id')

            serializer=BuyTransactionSerializer(transaction,many=True)
            data={'data':serializer.data}
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response({'error':"Error user must be admin"})

    except Exception as e:
        error=str(e)
        return Response({'error':f"UNexpected error Occured {error}"},status=status.HTTP_400_BAD_REQUEST)
