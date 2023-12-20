from django.urls import path
from . import views

urlpatterns = [
    path('createNewProductItem/',views.CreateNewProductItem),   
    path('createNewProductType/',views.CreateNewProductType),
    path('addProductItemToProductType/<int:productTypeId>/<int:productItemId>/',views.AddProductItemToProductType),
    path('createNewBuyTransaction/',views.CreateNewBuyTransaction),
    path('getBuyTransactionHistory/',views.GetBuyTransactionHistory),
    path('getBuyTransactionHistory/<int:limit>',views.GetBuyTransactionHistory),
    path('cancelBuyTransaction/',views.CancelBuyTransaction),
    path('approveBuyTransaction/<int:transactId>',views.ApproveBuyTransaction),
]
