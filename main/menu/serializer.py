from main.abstract.serializer import AbstractSerializer
from rest_framework import serializers
from .models import Menu
from main.categories.models import Category

class MenuSerializer(AbstractSerializer):
    CategoryId = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='PublicId')
    class Meta:
        model = Menu
        fields = ['FoodName', 'FoodDescription', 'FoodPrice', 'Created', 'Updated', 'FuncStatus', 'FoodStatus', 'id', 'CategoryId']
        read_only_field = ['Created', 'id']
