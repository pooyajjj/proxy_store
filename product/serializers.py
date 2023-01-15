from .models import products
from rest_framework import serializers


class ProductsSerializers(serializers.ModelSerializer):

    name = serializers.CharField()
    descraption = serializers.CharField()
    is_stock = serializers.BooleanField()
    slug = serializers.SlugField()
    price = serializers.IntegerField()
    img = serializers.ImageField()
    created = serializers.DateTimeField()
    update = serializers.DateTimeField()


    class Meta:
        model = products
        fields = '__all__'