from django.urls import path
from . import views
urlpatterns = [
    path('createNewRequest/',views.createNewRequest),
    path('getRequestTransactionHistory/',views.GetAllRequestTransaction),
    path('acceptRequestTransaction/<int:transactId>',views.AcceptRequestTransaction),
    path('denyRequestTransaction/<int:transactId>',views.DenyRequestTransaction),
    
]
