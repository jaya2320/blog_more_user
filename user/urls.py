from django.urls import path
from .views import *
urlpatterns = [
    path('', index,name='index'),
    path('customer', CustomerSignUpView.as_view(), name='customer_signup'),
    path('manager', ManagerSignUpView.as_view(), name='manager_signup'),
]
