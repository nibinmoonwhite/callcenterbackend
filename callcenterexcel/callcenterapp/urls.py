from django.test import TestCase

# Create your tests here.
from django.urls import path
from django.conf import settings
from rest_framework import views

from rest_framework_simplejwt import views as jwt_views


from .views import *

from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/',RegisterView.as_view(), name='register'),
    path('api/login/',Login.as_view(), name='login'),


    path('listdesignation/', Listdesignation.as_view()),   


    path('changepassword/<int:pk>/',ChangePasswordView.as_view()), 
    path('listusers/', Listuserss.as_view()),
    path('getuser/<int:pk>/', Getuserbyid.as_view()),
    path('updateuser/<int:pk>/', Updateuser.as_view()),   



    path('api/liststatus/',ListStatus.as_view(), name='liststatus'),
    path('api/addcustomerdetails/',AddCustomerdetails.as_view(), name='addcustomers'),
    path('api/listcustomerdetails/',ListCustomerdetails.as_view(), name='listcustomer'),
    path('api/patchcustomerdetails/<int:pk>/',PatchCustomerdetails.as_view(), name='patchcustomers'),
    path('api/deletecustomerbyid/<int:pk>/', Deletecustomer.as_view()),
    path('getcustomer/<int:pk>/', Getcustomerbyid.as_view()),


    path('api/listfollowupcustomerdetails/',ListFollowupcustomerdetails.as_view(), name='licustomer'),
    path('api/addfollowupcustomerdetails/',AddFollowupcustomerdetails.as_view(), name='followupcost'),
    path('api/patchfolloup/<int:pk>/',PatchFollowupcustomerdetails.as_view(), name='patchcustomers'),

    path('export/', ExportExcel.as_view()),
    path('import/', ImportExcel.as_view()),  
]
