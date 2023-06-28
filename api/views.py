from rest_framework.views import APIView
from orders.models import Product
from .serializers import ProductSerializers
from rest_framework.response import Response


class ProductView(APIView):
    def get(self, request):
        output = [
            {
            'name': output.name,
            'image': output.image,
            'description': output.description,
            'price': output.price,
            'date': output.date,
            } for output in Product.objects.all()
        ]
        return Response(output)

    def get(self, request):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

