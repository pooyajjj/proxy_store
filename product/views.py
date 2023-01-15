from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import products as pro #be carefull
from .serializers import ProductsSerializers
from rest_framework import status


class Products(APIView):
    product = pro.objects.filter(is_stock = True)

    def get(self, request):
        serz_data = ProductsSerializers(instance=self.product)

        return Response(serz_data.data, status=status.HTTP_200_OK)