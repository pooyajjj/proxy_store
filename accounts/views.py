from django.shortcuts import render
from .models import User
from rest_framework import status, viewsets
from .serializers import UserSerializer, UserRefisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class RegisterView(APIView):
    def post(self, request):
        ser_data = UserRefisterSerializer(data = request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()

    def list(self, request):
        srz_data = UserSerializer(instance=self.queryset, many=True)
        return Response(data=srz_data.data)


class AllUser(APIView):
    data = User.objects.all()

    def get(self, request):
        srz_data = UserSerializer(instance=self.data, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)