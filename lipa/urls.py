from django.urls import path
from .views import payment,success

urlpatterns=[
    path("lipa",payment,name="payments"),
    path("payment/success",success,name="payment-success")
]