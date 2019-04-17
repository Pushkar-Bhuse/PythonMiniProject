from django.views.generic import View
from django.shortcuts import render
from .api.location import *
from .models import *
from django.core.mail import send_mail
from django.conf import settings



tax = 0.18

class Cart(View):
    def get(self, request, *args, **kwargs):
        template = "delivery/cart.html"
        starters = Product.objects.filter(course = "starters")
        main = Product.objects.filter(course = "Main")
        dessert = Product.objects.filter(course = "dessert")
        currentorder = Order.objects.filter(owner__id = request.user.id, is_ordered = False).order_by("date_ordered")
        currentproducts = []
        if not currentorder:
            currentorder = {}
        else:
            currentorder = currentorder[0]
            for item in currentorder.items.all():
                currentproducts.append(item.product.id)
        context = {'starters': starters, 'main':main, 'dessert': dessert, 'currentproducts':currentproducts}
        return render(request, template, context)

class FinalOrder(View):
    def get(self, request, *args, **kwargs):
        template = "delivery/finalorder.html"
        myorder = Order.objects.filter(owner__id = request.user.id, is_ordered = False).order_by("date_ordered")
        if not myorder:
            order = {}
        else:
            order = myorder[0]
        # import pdb; pdb.set_trace()
        context = {'user': request.user, "myorder" : order, "tax":tax}
        return render(request, template, context)

class PlaceOrder(View):
    def get(self,request,*args,**kwargs):
        order = Order.objects.get(owner__id = request.user.id, is_ordered = False)
        refcode = order.ref_code
        items = order.items
        total = order.total
        total = float(total)
        total = round(total*1.18,2)
        message = "Thanks for placing an order (ref. code {}). Please pay ${} to our delivery personnel.".format(refcode,total)
        subject = "Food Hall"
        emailFrom = settings.EMAIL_HOST_USER
        emailTo = [request.user.email]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=False,)
        order.is_ordered = True
        order.save()
        return render(request,'reservation/index.html',{})
