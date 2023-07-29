from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from base.models import Product
from base.Products import Products
from base.serializer import ProductSerializer,UserSerializer,UserSerializerWithToken
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from typing import Any, Dict, Optional, Type, TypeVar
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status