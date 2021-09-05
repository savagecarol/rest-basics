from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import *
from .serializers import *


class FoodStoreView(APIView):
    def get(self, request, format=None):
        obj = FoodStore.objects.all()
        serializer = FoodStoreSerializer(obj, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = FoodStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)




class FoodStoreEditView(APIView):
    def get(self, request , pk , format=None):
        obj = FoodStore.objects.get(id = pk)
        serializer = FoodStoreSerializer(obj)
        return Response(serializer.data, status.HTTP_200_OK)


    def put(self, request, pk, format=None):
        obj = FoodStore.objects.get(id=pk)
        serializer = FoodStoreSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return  Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = FoodStore.objects.get(id = pk)
        obj.delete()
        return Response(status.HTTP_400_BAD_REQUEST)

















class ItemView(APIView):
    def get(self, request, format=None):
        obj = Item.objects.all()
        serializer = ItemSerializer(obj, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)




class ItemEditView(APIView):
    def get(self, request , pk , format=None):
        obj = Item.objects.get(id = pk)
        serializer = ItemSerializer(obj)
        return Response(serializer.data, status.HTTP_200_OK)


    def put(self, request, pk, format=None):
        obj = Item.objects.get(id=pk)
        serializer = ItemSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return  Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = Item.objects.get(id = pk)
        obj.delete()
        return Response(status.HTTP_400_BAD_REQUEST)






