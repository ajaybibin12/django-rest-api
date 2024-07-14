from django.http import JsonResponse
from .models import Products
from .serializers import ProductSerializer
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

@csrf_exempt
@api_view(['POST'])
def user_signup(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            token,created = Token.objects.get_or_create(user=user)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def get_products(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)
