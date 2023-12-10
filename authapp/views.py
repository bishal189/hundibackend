# Import your Account model or replace with the correct import
from .models import Account
from django.contrib.auth.decorators import login_required
from authapp.forms import ResitrationForm
from .models import Account
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from django.contrib import  auth
#
from rest_framework.response import Response
from rest_framework import status

#
@csrf_exempt
@api_view(['POST'])

def Register(request):
    if request.method == 'POST':
        
            form = ResitrationForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']

                confirm_password=request.POST['confirm_password']

                country=form.cleaned_data['country']
                phone_number=form.cleaned_data['phone_number']

                if password!=confirm_password:
                    data={"error":"password and confirm password must be equal"}
                    return Response(data,status=status.HTTP_400_BAD_REQUEST)


                user = Account.objects.create_user(
                    email=email, name=name, password=password,country=country,phone_number=phone_number)
                user.save()
                auth.login(request,user)
                # user activation
                data={'message':"You have signed up sucessfully"}
                return Response(data,status=status.HTTP_201_CREATED)

            else:
                data={'error':"Unique contraint failed for name or phonenumber"}
                return Response(data,status=status.HTTP_403_FORBIDDEN)       
    else:
        data={"error":"Method Not Allowed . Try again"}
        return Response(data,status=status.HTTP_400_BAD_REQUEST)
       


#For login 
@api_view(['POST'])
@csrf_exempt
def Login(request):
    print(request.POST)
    if request.method == 'POST':
            # CAPTCHA verification passed
            email_or_phone = request.POST['email_or_phone']
            password = request.POST['password']
            if '@' in email_or_phone:
            # Authenticate the user and perform other login logic
                user = auth.authenticate(email=email_or_phone, password=password)
            else:
                user_phone=Account.objects.get(phone_number=email_or_phone)
                user=auth.authenticate(email=user_phone.email,password=password)


            if user is not None:
                
                    auth.login(request, user)
                    data={"message":"Login Sucessfull"}
                    return Response(data,status=status.HTTP_200_OK)
            else:
                data={"error":"Login credentials are incorrect"}
                return Response(data,status=status.HTTP_401_UNAUTHORIZED)
        


# logout function is here
@csrf_exempt
@api_view(['GET'])
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    data={"error":"you are logged out!"}
    return Response(data,status=status.HTTP_200_OK)
