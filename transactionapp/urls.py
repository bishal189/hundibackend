
from django.urls import path
from . import views
urlpatterns = [

    path('newTransaction/',views.CreateNewTransaction,name='newTransaction'),
    path('cancelTransaction/',views.CancelTransaction,name='cancelTransaction'),
    path('getBankCards/<str:countryCode>/',views.GetBankCards,name='getBankCards'),
    path('verifyTransaction',views.VerifyTransaction,name='verifyTransaction')
]
