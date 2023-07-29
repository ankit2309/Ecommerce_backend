from django.shortcuts import render
from base.models import Product

from base.serializer import ProductSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def getproducts(request):
    products = Product.objects.all()
    serailizer = ProductSerializer(products,many=True)
    return Response(serailizer.data)

@api_view(['GET'])
def getproduct(request,pk):
    product = Product.objects.get(id=pk)
    serailizer =ProductSerializer(product,many=False)
    return Response(serailizer.data)