from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from pizza.models import Pizza
from pizza.serializers import PizzaSerializer
from rest_framework.decorators import api_view


@api_view(['POST'])
def create_pizza(request):
    # print(request.data)
    pizza_data = JSONParser().parse(request)
    # print(pizza_data)
    pizza_serializer = PizzaSerializer(data=pizza_data)
    if pizza_serializer.is_valid():
        if pizza_data['ptype'] not in ('Rectangle', 'Square'):
            return JsonResponse({'message': 'Type can be either \'Rectangle\' or \'Square\' only'}, status=status.HTTP_400_BAD_REQUEST)
        pizza_serializer.save()
        return JsonResponse(pizza_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(pizza_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_pizza(request):
    pizza = Pizza.objects.all()
    
    size = request.GET.get('size', None)
    if size is not None:
            pizza = pizza.filter(size__icontains=size)

    ptype = request.GET.get('ptype', None)
    if ptype is not None:
            pizza = pizza.filter(ptype__icontains=ptype)
    
    tutorials_serializer = PizzaSerializer(pizza, many=True)
    return JsonResponse(tutorials_serializer.data, safe=False)
    # 'safe=False' for objects serialization


@api_view(['PUT'])
def edit_pizza(request, pk):
    try:
        pizza = Pizza.objects.get(pk=pk)
        pizza_data = JSONParser().parse(request) 
        pizza_serializer = PizzaSerializer(pizza, data=pizza_data) 
        if pizza_serializer.is_valid(): 
            pizza_serializer.save() 
            return JsonResponse(pizza_serializer.data, status=status.HTTP_200_OK) 
        return JsonResponse(pizza_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    except:
        return JsonResponse({'message': 'Pizza does not exist!'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_pizza(request, pk):
    try:
        pizza = Pizza.objects.get(pk=pk)
        pizza.delete() 
        return JsonResponse({'message': 'Pizza deleted successfully!'}, status=status.HTTP_200_OK)
    except:
        return JsonResponse({'message': 'Pizza does not exist!'}, status=status.HTTP_400_BAD_REQUEST) 
