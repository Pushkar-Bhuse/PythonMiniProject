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
from delivery.api.location import *
from datetime import datetime
from django.db.models import Q
from reservation.models import Reservation,Branch
user = get_user_model()

class CartItems(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def get_queryset(self, *args, **kwargs):
        tweet_id = self.kwargs.get("pk")
        qs = Order.objects.filter(owner__id=tweet_id, is_ordered = False).order_by("date_ordered")
        return qs


class UpdateOrder(APIView):
    def post(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        order_item = json.loads(request.POST['item'])
        item = order_item["item"]
        value = order_item["quantity"]
        if value == 0:
            temp = Product.objects.filter(id = item)[0]
            obj = Order.objects.filter(is_ordered = False, owner = request.user)[0]
            for item in obj.items.all():
                if item.product == temp:
                    item.delete()
                    item.save()
        else:
            temp = Product.objects.filter(id = item)
            obj = Order.objects.filter(is_ordered = False, owner = request.user)[0]
            for item in obj.items.all():
                if item.product == temp:
                    item.quantity = value
                    item.set_individual_price()
                    item.save()

        obj = Order.objects.get(is_ordered = False, owner = request.user)
        obj.set_cart_total()
        obj.save()

        return JsonResponse({'success':True})


class AddToCart(APIView):
    def post(self,request, *args, **kwargs):
        product = request.POST["product"]
        obj, created = Order.objects.get_or_create(is_ordered = False, owner = request.user)
        now = datetime.now()

        if created:
            obj.ref_code = now.strftime("%d") + str(request.user.id)
            obj.save()

        # for product in product_list:
        temp = Product.objects.get(id = product)
        item = OrderItem.objects.create(quantity = 1, product = temp, price = temp.cost)
        obj.items.add(item)
        obj.set_cart_total()
        obj.save()

        return JsonResponse({'success':True})

class RemoveFromCart(APIView):
    def post(self,request, *args, **kwargs):
        product = request.POST["product"]
        # import pdb; pdb.set_trace()
        obj= Order.objects.get(is_ordered = False, owner = request.user)

        # for product in product_list:
        temp = Product.objects.get(id = product)
        item = OrderItem.objects.get(product = temp)
        obj.items.remove(item)
        item.delete()
        obj.set_cart_total()
        obj.save()

        return JsonResponse({'success':True})


#  class DeliveryConfirmation(APIView):
#      def post(self, request, *args, *kwargs):
#          refcode = tweet_id = self.kwargs.get("ref_code")

class ChartData(APIView):
    def get(self,request,*args,**kwargs):
        place = self.kwargs.get("place")
        # label = ["12:00 PM","1:00 PM","2:00 PM","3:00 PM","4:00 PM","5:00 PM","6:00 PM","7:00 PM","8:00 PM","9:00 PM","10:00 PM","11:00 PM","00:00 AM",]
        label = []
        data = []
        population = {}

        for i in range (12,24):
            if i == 23:
                temp = "{}PM-{}AM".format(i-12,0)
            else:
                temp = "{}PM-{}PM".format(i-12,i+1-12)
            label.append(temp)
            count = Reservation.objects.filter(Q(time__hour__gte = i) & Q(time__hour__lt = i+1), place__id = place).count()
            data.append(count)
        # import pdb; pdb.set_trace()
        return JsonResponse({"label":label,"data":data})




