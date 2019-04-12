from django.conf.urls import url
from django.conf import settings
from django.urls import path,include
from delivery.api.views import TestApiView,UpdateOrder,AddToCart
from .views import DeliveryConfirmation

urlpatterns = [
    url(r'get/(?P<pk>\d+)/$', TestApiView.as_view(), name='test'),
    url('put/', UpdateOrder.as_view(), name='update'),
    url('add_to_cart/', AddToCart.as_view(), name='update'),
    url(r'confirmation/(?P<ref_code>\d+)/$', DeliveryConfirmation.as_view(), name = 'confirmation'),
]