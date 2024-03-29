# Import your Account model or replace with the correct import
from django.contrib.auth.decorators import login_required
from authapp.forms import ResitrationForm
from .models import Account
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
from django.contrib import  auth

from .forms import UpdateForm
#
from rest_framework.response import Response
from rest_framework import status
from django.middleware.csrf import get_token
from rest_framework_simplejwt.tokens import RefreshToken
from transactionapp.serializers import AccountSerializer
# from transactionapp.serializers import AccountSerializer
# from .serializers import UserProfileSerializer
#
@csrf_exempt
@api_view(['POST'])

def Register(request):
    if request.method == 'POST':
            data=json.loads(request.body)

            form = ResitrationForm(data)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']

                password = form.cleaned_data['password']
                confirm_password=data['confirmPassword']

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
                refresh = RefreshToken.for_user(user)
                data = {
                    'token': {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                }
            }
                return Response(data, status=status.HTTP_201_CREATED)

            else:
                data={'error':f'Unique contraint failed for name or phonenumber ${form.errors}'}
                return Response(data,status=status.HTTP_403_FORBIDDEN)       
    else:
        data={"error":"Method Not Allowed . Try again"}
        return Response(data,status=status.HTTP_400_BAD_REQUEST)
       


#For login 
@api_view(['POST'])
@csrf_exempt
def Login(request):
    if request.method == 'POST':
            data=json.loads(request.body)
            # CAPTCHA verification passed
            email_or_phone = data['email_or_phone']
            password = data['password']
            if '@' in email_or_phone:
            # Authenticate the user and perform other login logic
                user = auth.authenticate(email=email_or_phone, password=password)
                print(user)
            else:
                user_phone=Account.objects.get(phone_number=email_or_phone)
                user=auth.authenticate(email=user_phone.email,password=password)

            if user is not None:
                auth.login(request,user)
                refresh = RefreshToken.for_user(user)
                data = {
                    'token': {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        
@api_view(['GET'])
def verifyUser(request):
    if request.user is not None:
        data={"message":"verified user is there"}
        return Response(data,status=status.HTTP_200_OK)
    else:
        return Response({'error':"User not Verified"},status=status.HTTP_401_UNAUTHORIZED)
# logout function is here
@csrf_exempt
@api_view(['GET'])
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    data={"error":"you are logged out!"}
    return Response(data,status=status.HTTP_200_OK)


@api_view(['GET'])
def get_csrf_token(request):
    csrf_token = get_token(request)
    return Response({'csrf_token': csrf_token})


@api_view(['GET'])
def get_user(request,userId=None):
    if userId is None:
        serializer=AccountSerializer(request.user)
    else:
        if request.user.is_admin==True:
            user=Account.objects.get(id=userId)
            serializer=AccountSerializer(user)
        else:
            return Response({"error":"Only admin can view other user detail"},status=400)

    return Response({'data':serializer.data})

@api_view(['GET'])
def get_all_users(request):
    try:
        if request.user.is_admin:
            users=Account.objects.all().order_by('-id')
            serializer=AccountSerializer(users,many=True)
            return Response({'data':serializer.data},status=200)
        else:
            return Response({'error':"Only admin can view all users"},status=403)

    except Exception as e:
        error=str(e)
        print(error)
        return Response({'error':f"Unexpcted error occured {error}"},status=400)




@api_view(['POST'])
def update_profile(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        user_profile = request.user
        print(user_profile)

        if ('password' in data and 'confirmPassword' not in data) or('password' not in data and 'confirmPassword' in data):
            return Response({'error':"password and confirm password cannot come alone"},status=status.HTTP_400_BAD_REQUEST)

        
        if 'password'in data and'confirmPassword' in data :
            if data['password']!=data['confirmPassword']:
                return Response({'error':"password and confirm password didnot match"},status=status.HTTP_400_BAD_REQUEST)

        # Update only the fields present in the request data
        for field in Account._meta.fields:  # Iterate over model fields
            field_name = field.name
            if field_name in data:
                setattr(user_profile, field_name, data[field_name])

        if 'password' in data:
            user_profile.set_password(data['password'])
        user_profile.save()            
            # Serialize the updated user data

        return Response({
                'message': 'The user details are updated',
            }, status=200)
    else:
        form = UpdateForm(instance=request.user)

    return Response({'form': form})


     
