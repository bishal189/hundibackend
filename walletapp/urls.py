from django.urls import path
from . import views
urlpatterns = [
    path('createNewTopUpTransaction/',views.CreateNewTopUpTransaction),
    path('acceptTopUpTransaction/<int:transactionId>/',views.AcceptTopUpTransaction),
    path('getTopUpTransactionHistory/',views.GetTopUpTransactionHistory),

    path('createNewWithDrawTransaction/',views.CreateNewWithDrawTransaction),
    path('acceptWithDrawTransaction/<int:transactionId>/',views.AcceptWithDrawTransaction),
    path('getWithDrawTransactionHistory/',views.GetWithDrawTransactionHistory),

    path('createNewSendTransaction/',views.CreateNewSendTransaction),
    path('acceptSendTransaction/<int:transactionId>/',views.AcceptSendTransaction),
    path('getSendTransactionHistory/',views.GetSendTransactionHistory),
]
