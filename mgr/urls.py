from django.urls import path

from mgr import customer, sign_in_out

urlpatterns = [

    path('customers', customer.dispatcher),
    path('signout', sign_in_out.signout),

]
