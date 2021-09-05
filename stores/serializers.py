from rest_framework import serializers

from .models import FoodStore, Item


class FoodStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodStore
        fields = ['id', 'name', 'email', 'contact', 'address']


class FoodStoreNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodStore
        fields = ['name']

class ItemSerializer(serializers.ModelSerializer):
    store = FoodStoreNameSerializer()
    class Meta:
        model = Item
        fields = ['id', 'name', 'quantity', 'price', 'store']
