from django.urls import path
from . import views

urlpatterns = [
    path('createNewProductItem/',views.CreateNewProductItem),   
    path('createNewProductType/',views.CreateNewProductType),
    path('listProductItem/<int:productTypeId>/',views.ListProductItem),
    path('listProductType/',views.ListProductType),
    path('showProductItemDetail/<int:productItemId>/',views.ShowProductItemDetail),
    path('addProductItemToProductType/<int:productTypeId>/<int:productItemId>/',views.AddProductItemToProductType),
    path('createNewBuyTransaction/',views.CreateNewBuyTransaction),
    path('getBuyTransactionHistory/',views.GetBuyTransactionHistory),
    path('getBuyTransactionHistory/<int:limit>/',views.GetBuyTransactionHistory),

    path('cancelBuyTransaction/',views.CancelBuyTransaction),
    path('approveBuyTransaction/<int:transactId>/',views.ApproveBuyTransaction),

    path('denyBuyTransaction/<int:transactId>/',views.DenyBuyTransaction),


    #admin
    path('getBuyTransactionAdminHistory/',views.GetBuyTransactionAdminHistory),

]
