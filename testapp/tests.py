from django.test import TestCase
from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APITestCase
from product.serializers import ProductsSerializers
from product.models import products

class ProductsViewTestCase(APITestCase):
    
    def setUp(self):
        self.client = Client()
        self.products = [
            products(name='product1', price=10.0, is_stock=True),
            products(name='product2', price=20.0, is_stock=False),
            products(name='product3', price=30.0, is_stock=True)
        ]
        products.objects.bulk_create(self.products)

    def test_products_view(self):
        # Test GET request
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Test that only products with is_stock=True are returned
        expected_products = pro.objects.filter(is_stock=True)
        serz_data = ProductsSerializers(instance=expected_products, many=True)
        self.assertEqual(response.data, serz_data.data)
