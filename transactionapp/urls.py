
from django.urls import path
from . import views
urlpatterns = [

    path('newTransaction/',views.CreateNewTransaction,name='newTransaction'),
    path('cancelTransaction/',views.CancelTransaction,name='cancelTransaction'),
    path('cancelBuyTransaction/',views.CancelBuyTransaction,name='cancelBuyTransaction'),
    path('getBankCards/<str:countryCode>/',views.GetBankCards,name='getBankCards'),
    path('verifyTransaction/',views.VerifyTransaction,name='verifyTransaction'),
    path('getTransactionHistory/',views.GetTransactionUserHistory,name='history'),
    path('getBuyTransactionHistory/',views.GetBuyTransactionUserHistory,name='buy_history'),
    path('newBuyTransaction/',views.CreateNewBuyTransaction,name='buy_newTransaction'),

    
]
