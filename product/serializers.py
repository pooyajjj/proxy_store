from .models import products
from rest_framework import serializers


class ProductsSerializers(serializers.Serializer):

    class Meta():
        model = products
        fields = '__all__'