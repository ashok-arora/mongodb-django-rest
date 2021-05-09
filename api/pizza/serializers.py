from rest_framework import serializers 
from pizza.models import Pizza 
 
class PizzaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Pizza
        fields = ('id',
                  'ptype',
                  'size',
                  'toppings')