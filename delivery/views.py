from django.views.generic import View
from django.shortcuts import render
from .api.location import *
from .models import *



class Cart(View):
    def get(self, request, *args, **kwargs):
        template = "delivery/cart.html"
        products = Product.objects.all()
        currentorder = Order.objects.filter(owner__id = request.user.id, is_ordered = False).order_by("date_ordered")[0]
        currentproducts = []
        for item in currentorder.items.all():
            currentproducts.append(item.product.id)
        context = {'products': products, 'currentproducts':currentproducts}
        return render(request, template, context)

class FinalOrder(View):
    def get(self, request, *args, **kwargs):
        template = "delivery/finalorder.html"
        myorder = Order.objects.filter(owner__id = request.user.id, is_ordered = False).order_by("date_ordered")
        context = {'user': request.user, "myorder" : myorder[0]}
        return render(request, template, context)

