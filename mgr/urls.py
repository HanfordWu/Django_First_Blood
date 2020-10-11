from django.db import transaction
from django.http import JsonResponse
from django.urls import path

from common.models import OrderMedicine, Order
from mgr import customer, sign_in_out, medicine, order

urlpatterns = [

    path('customers', customer.dispatcher),
    path('signout', sign_in_out.signout),
    path('signin', sign_in_out.signin),
    path('medicines', medicine.dispatcher),
    path('orders', order.dispatcher),
]