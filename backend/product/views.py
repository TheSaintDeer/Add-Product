from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_list_or_404

from . import serializers, models


class ProductList(APIView):

    def get(self, request):
        queryset = get_list_or_404(models.Product)
        data = serializers.ProductSerializer(queryset, many=True)

        print(data.data)

        return Response(data=data.data, status=status.HTTP_200_OK)
    

class ProductCreate(APIView):

    def post(self, request, format=None):
        if request.data:
            data = serializers.ProductSerializer(data=request.data)

            if data.is_valid():
                data.save()
                return Response(data=data.data, status=status.HTTP_201_CREATED)
            
            return Response(data="Incorrect data", status=status.HTTP_400_BAD_REQUEST)

        return Response(data="Request data is empty.", status=status.HTTP_400_BAD_REQUEST)