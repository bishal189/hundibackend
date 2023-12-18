from django.urls import path
from . import views
urlpatterns = [
    path('createNewRequest/',views.createNewRequest),
    path('getAllRequestTransaction/',views.GetAllRequestTransaction),
    path('acceptRequestTransaction/<int:transactId>',views.AcceptRequestTransaction),
    
]
