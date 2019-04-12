from rest_framework.views import APIView
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from urllib import request
from datetime import datetime
from rest_framework import generics
from delivery.models import Order,Product,OrderItem
from .serializers import OrderSerializer, ProductSerializer,OrderItemSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .api.location import *

user = get_user_model()

class TestApiView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def get_queryset(self, *args, **kwargs):
        tweet_id = self.kwargs.get("pk")
        qs = Order.objects.filter(pk=tweet_id, is_ordered = False).order_by("date_ordered")
        return qs


class UpdateOrder(APIView):
    def post(self, request, *args, **kwargs):
        ref_code = request.POST['ref_code']
        order_item = json.loads(request.POST['items'])
        owner = json.loads(request.POST['owner'])


        for key,value in order_item.items():
            # item = OrderItem.objects.get(id = int(key))
            if value == 0:
                OrderItem.objects.filter(id = int(key)).delete()
            else:
                OrderItem.objects.filter(id = int(key)).update(quantity = value)

        return JsonResponse({'success':True})


class AddToCart(APIView):
    def post(self,request, *args, **kwargs):

        product_list = request.POST.getlist("products[]")
        import pdb; pdb.set_trace()
        obj = Order.objects.get(is_ordered = False, owner = request.user)

        if not obj:
            obj.ref_code = 8907
            obj.owner = user
            obj.save()

        for product in product_list:
            temp = Product.objects.get(id = product)
            item = OrderItem.objects.create(quantity = 1, product = temp)
            obj.items.add(item)

        return JsonResponse({'success':True})


 class DeliveryConfirmation(APIView):
     def post(self, request, *args, *kwargs):
         refcode = tweet_id = self.kwargs.get("ref_code")




