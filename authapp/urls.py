from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.Login,name='login'),
    path('register/',views.Register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('get_token/',views.get_csrf_token,name='get_token'),
    path('verify_user/',views.verifyUser),
]
