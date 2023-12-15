
from django.urls import path
from . import views
urlpatterns = [

    path('newTransferTransaction/',views.CreateNewTransferTransaction,name='newTransaction'),
    path('cancelTransferTransaction/',views.CancelTransferTransaction,name='cancelTransaction'),
    path('cancelBuyTransaction/',views.CancelBuyTransaction,name='cancelBuyTransaction'),
    path('getBankCards/<str:countryCode>/',views.GetBankCards,name='getBankCards'),
    path('verifyTransferTransaction/',views.VerifyTransferTransaction,name='verifyTransaction'),
    path('getTransferTransactionHistory/<int:limit>',views.GetTransferTransactionUserHistory,name='historLimit'),
    path('getTransferTransactionHistory/',views.GetTransferTransactionUserHistory,name='history'),

    path('getBuyTransactionHistory/<int:limit>',views.GetBuyTransactionUserHistory,name='buy_historyLimit'),

    path('getBuyTransactionHistory/',views.GetBuyTransactionUserHistory,name='buy_history'),
    path('newBuyTransaction/',views.CreateNewBuyTransaction,name='buy_newTransaction'),

    
]
