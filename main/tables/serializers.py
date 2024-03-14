from rest_framework import serializers
from main.abstract.serializer import AbstractSerializer
from main.customers.serializers import RegisterCustomerSerializer
from .models import Table
class TableSerializer(AbstractSerializer):
    class Meta:
        model = Table
        fields = ['id' ,'TableNumber', 'TableSits', 'TableFee', 'Created', 'Updated', 'FuncStatus', 'TableStatus']
        read_only_field = ['Created', 'id']
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        table = Table.objects.get_by_id(rep['id'])
        customer = table.customer_set.filter(CustomerStatus=True)
        if customer.count() > 0: 
            rep['Customer'] = RegisterCustomerSerializer(customer[0]).data
        else: rep['Customer'] = None
        return rep

class RegisterTableSerializer(TableSerializer):
    class Meta:
        model = Table
        fields = ['id' ,'TableNumber', 'TableSits', 'TableFee', 'Created', 'Updated', 'FuncStatus', 'TableStatus']
        read_only_field = ['Created', 'id']
    def create(self, validated_data):
        return Table.objects.create(**validated_data)


