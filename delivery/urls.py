from django.conf.urls import url
from django.conf import settings
from django.urls import path,include
from .views import DeliveryConfirmation

urlpatterns = [
    url('cart/', Cart.as_view(), name='cart'),
]