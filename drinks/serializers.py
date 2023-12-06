from rest_framework import serializers
from .models import Drink
from .models import Customer
from .models import Order

class DrinkSerializer(serializers.ModelSerializer):
  class Meta:
    model = Drink
    fields = ['id', 'name', 'description']

class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields = ['name', 'phone', 'email']

class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = ['customer', 'product', 'status']