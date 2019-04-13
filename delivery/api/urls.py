from django.conf.urls import url
from django.conf import settings
from django.urls import path,include
from delivery.api.views import *


urlpatterns = [
    url(r'mycart/(?P<pk>\d+)/$', CartItems.as_view(), name='test'),
    url('update/', UpdateOrder.as_view(), name='update'),
    url('add_to_cart/', AddToCart.as_view(), name='add'),
    url('remove_from_cart/', RemoveFromCart.as_view(), name='remove'),
    url(r'chart_data/(?P<place>\d+)/$', ChartData.as_view(), name='chart_data'),
    # url(r'confirmation/(?P<ref_code>\d+)/$', DeliveryConfirmation.as_view(), name = 'confirmation'),
]