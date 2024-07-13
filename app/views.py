from django.http import JsonResponse
from .models import Products
from .serializers import ProductSerializer

def get_products(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)
