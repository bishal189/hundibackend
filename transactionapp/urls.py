
from django.urls import path
from . import views
urlpatterns = [
    path('userdashboard/',views.Dashboard,name="dashboard"),
    path('newTransferTransaction/',views.CreateNewTransferTransaction,name='newTransaction'),
    path('cancelTransferTransaction/',views.CancelTransferTransaction,name='cancelTransaction'),
    path('getBankCards/<str:countryCode>/',views.GetBankCards,name='getBankCards'),
    path('verifyTransferTransaction/',views.VerifyTransferTransaction,name='verifyTransaction'),
    path('getTransferTransactionHistory/',views.GetTransferTransactionUserHistory,name='history'),

    path('getTransferTransactionHistory/<int:limit>',views.GetTransferTransactionUserHistory,name='historLimit'),

    path('getPayTransactionHistory/<int:limit>',views.GetPayTransactionUserHistory,name='buy_historyLimit'),
    path('getPayTransactionHistory/',views.GetPayTransactionUserHistory,name='buy_history'),
    path('cancelPayTransaction/',views.CancelPayTransaction,name='cancelPayTransaction'),
    path('newPayTransaction/',views.CreateNewPayTransaction,name='buy_newTransaction'),


    #for admin now
    path('getTransferTransactionAdminHistory/',views.GetTransferTransactionAdminHistory),
    path('getPayTransactionAdminHistory/',views.GetPayTransactionAdminHistory),
    path('approveTransferTransactionAdmin/<transactId>/',views.ApproveTransferTransactionAdmin),
    path('denyTransferTransactionAdmin/<transactId>/',views.DenyTransferTransactionAdmin),
    path('approvePayTransactionAdmin/<transactId>/',views.ApprovePayTransactionAdmin),
    path('denyPayTransactionAdmin/<transactId>/',views.DenyPayTransactionAdmin),
]
