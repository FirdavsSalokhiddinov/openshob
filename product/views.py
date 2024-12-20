
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

# Manufacturer
@api_view(['GET'])
def getManufacturers(request):
   manufacturers = Manufacturer.objects.all()
   serializer = ManufacturerSerializer(manufacturers, many=True)
   return Response(serializer.data)

@api_view(['GET'])
def getManufacturer(request, pk):
   manufacturer = Manufacturer.objects.get(id=pk)
   serializer = ManufacturerSerializer(manufacturer, many=False)
   return Response(serializer.data)

@api_view(['GET'])
def getCategories(request):
    categories = Manufacturer.objects.values('category').distinct()
    return Response({'categories': list(categories)})


# Product
@api_view(['GET'])
def getProducts(request):
   products = Product.objects.all()
   serializer = ProductSerializer(products, many=True)
   return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
   product = Product.objects.get(id=pk)
   serializer = ProductSerializer(product, many=False)
   return Response(serializer.data)