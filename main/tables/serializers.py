from rest_framework import serializers
from main.abstract.serializer import AbstractSerializer
from .models import Table
class TableSerializer(AbstractSerializer):
    class Meta:
        model = Table
        fields = ['id' ,'TableNumber', 'TableSits', 'TableFee', 'Created', 'Updated', 'FuncStatus', 'TableStatus']
        read_only_field = ['Created', 'id']

class RegisterTableSerializer(TableSerializer):
    class Meta:
        model = Table
        fields = ['id' ,'TableNumber', 'TableSits', 'TableFee', 'Created', 'Updated', 'FuncStatus', 'TableStatus']
        read_only_field = ['Created', 'id']
    def create(self, validated_data):
        return Table.objects.create(**validated_data)


