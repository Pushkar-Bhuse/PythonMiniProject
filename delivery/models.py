from django.db import models
from django.conf import settings



class Product(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 150, null = True)
    cost = models.DecimalField(max_digits=4, decimal_places=2)
    preparation_time = models.IntegerField(max_length=4)
    course = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, null = True)

    def create(self):
        self.price = self.product.cost

    def set_individual_price(self):
        self.price = self.quantity*self.price
        return

    def __str__(self):
        return self.product.name


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem, null = True)
    date_ordered = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=4, decimal_places=2, default = 0)



    def set_cart_total(self):
        number = sum([item.product.cost for item in self.items.all()])
        self.total = round(number,2)
        return

    # def get_ref_code(self):
    #     date = str(item.SCHEDULED_AT.strftime("%B%d%Y"))+

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)
