from django.contrib.auth import get_user_model
from rest_framework import serializers
from delivery.models import Product,Order,OrderItem

User = get_user_model()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only = True)
    #import pdb; pdb.set_trace()
    class Meta:
        model = OrderItem
        fields = ['product' , 'quantity', 'id']


class OrderSerializer(serializers.ModelSerializer):
    owner  = UserDisplaySerializer(read_only = True)
    items = OrderItemSerializer(read_only = True, many = True)
    class Meta:
        model = Order
        fields = ['ref_code', 'owner', 'items']