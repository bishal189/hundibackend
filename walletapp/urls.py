from django.urls import path
from . import views
urlpatterns = [
    path('createNewTopUpTransaction/',views.CreateNewTopUpTransaction),
    path('acceptTopUpTransaction/<int:transactionId>/',views.AcceptTopUpTransaction),
    path('getTopUpTransactionHistory/',views.GetTopUpTransactionHistory),
]
