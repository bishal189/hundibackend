from django.urls import path
from . import views
urlpatterns = [
    path('createNewRequest/',views.createNewRequest),
    path('getRequestTransactionHistory/',views.GetAllRequestTransaction),
    path('acceptRequestTransaction/<transactId>/',views.AcceptRequestTransaction),
    path('denyRequestTransaction/<transactId>/',views.DenyRequestTransaction),
    
]
