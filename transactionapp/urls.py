
from django.urls import path
from . import views
urlpatterns = [
    path('userdashboard/',views.Dashboard,name="dashboard"),
    path('newTransferTransaction/',views.CreateNewTransferTransaction,name='newTransaction'),
    path('cancelTransferTransaction/',views.CancelTransferTransaction,name='cancelTransaction'),
    path('cancelPayTransaction/',views.CancelPayTransaction,name='cancelPayTransaction'),
    path('getBankCards/<str:countryCode>/',views.GetBankCards,name='getBankCards'),
    path('verifyTransferTransaction/',views.VerifyTransferTransaction,name='verifyTransaction'),
    path('getTransferTransactionHistory/<int:limit>',views.GetTransferTransactionUserHistory,name='historLimit'),
    path('getTransferTransactionHistory/',views.GetTransferTransactionUserHistory,name='history'),

    path('getPayTransactionHistory/<int:limit>',views.GetPayTransactionUserHistory,name='buy_historyLimit'),

    path('getPayTransactionHistory/',views.GetPayTransactionUserHistory,name='buy_history'),
    path('newPayTransaction/',views.CreateNewPayTransaction,name='buy_newTransaction'),

    
]
