from django.urls import path
from . import views
urlpatterns = [
    path('createNewTopUpTransaction/',views.CreateNewTopUpTransaction),
    path('acceptTopUpTransaction/<int:transactionId>/',views.AcceptTopUpTransaction),
    path('denyTopUpTransaction/<int:transactionId>/',views.DenyTopUpTransaction),

    path('getTopUpTransactionHistory/',views.GetTopUpTransactionHistory),

    path('createNewWithDrawTransaction/',views.CreateNewWithDrawTransaction),
    path('acceptWithDrawTransaction/<int:transactionId>/',views.AcceptWithDrawTransaction),
    path('denyWithDrawTransaction/<int:transactionId>/',views.DenyWithDrawTransaction),

    path('getWithDrawTransactionHistory/',views.GetWithDrawTransactionHistory),

    path('createNewSendTransaction/',views.CreateNewSendTransaction),
    path('acceptSendTransaction/<int:transactionId>/',views.AcceptSendTransaction),
     path('denySendTransaction/<int:transactionId>/',views.DenySendTransaction),

    path('getSendTransactionHistory/',views.GetSendTransactionHistory),
]
