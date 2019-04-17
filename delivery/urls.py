from django.conf.urls import url
from django.conf import settings
from django.urls import path,include
from delivery.views import Cart,FinalOrder,PlaceOrder

app_name = "delivery"

urlpatterns = [
    url('cart/', Cart.as_view(), name = 'cart'),
    url('finalorder/', FinalOrder.as_view(), name = 'finalorder'),
    url('checkout/', PlaceOrder.as_view(), name = 'checkout'),
]