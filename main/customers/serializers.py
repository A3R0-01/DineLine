from main.abstract.serializer import AbstractSerializer
from main.customers.models import Customer
from main.tables.models import Table
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from django.db import transaction
from main.orders.serializers import OrdersMainSerializer
from main.orders.models import Order
from main.user.models import User
from main.clearance.models import Clearance

class RegisterCustomerSerializer(AbstractSerializer):
    TableId = serializers.SlugRelatedField(queryset=Table.objects.exclude(FuncStatus=False), slug_field='PublicId')

    class Meta:
        model = Customer
        fields = ['id', 'CustomerName', 'TableId', 'Created', 'Updated', 'CustomerStatus']
        read_only_field = ['Created', 'id', 'CustomerStatus']

    def to_representation(self, instance):
        rep  =  super().to_representation(instance)
        print(rep)
        customer = Customer.objects.get_by_id(rep['id'])
        orders_per_customer = Order.objects.filter(FuncStatus=True, Customer=customer)
        rep['Orders'] = [OrdersMainSerializer(i).data for i in orders_per_customer]
        return rep


    @transaction.atomic
    def create(self, validated_data):
        if not Customer.objects.filter(TableId=validated_data['TableId'], CustomerStatus=True).exists() and Table.objects.filter(PublicId=validated_data['TableId'].PublicId, TableStatus=False).exists():
            Table.objects.occupy_table(validated_data['TableId'].PublicId)
            customer = Customer.objects.create(**validated_data)
            employee = User.objects.get_employee_by_id(self.context['request'].user.EmployeeId)
            clearance = Clearance.objects.create(Customer=customer, Employee=employee)
            print(f'Clearance Created: {clearance}')
            return customer
        else:
            raise ValidationError('Table is occupied')