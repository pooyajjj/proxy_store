from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import products
from .serializers import ProductsSerializers
from rest_framework import status


class ProductsView(APIView):
    product = get_object_or_404(products, is_stock=True)

    def get(self, request):
        serz_data = ProductsSerializers(instance=self.product, many=True)

        return Response(serz_data.data, status=status.HTTP_200_OK)