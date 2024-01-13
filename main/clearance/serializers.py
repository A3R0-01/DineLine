from main.abstract.serializer import AbstractSerializer
from main.customers.models import Customer
from main.user.models import User
from rest_framework.serializers import SlugRelatedField
from .models import Clearance

class ClearanceSerializer(AbstractSerializer):
    Customer = SlugRelatedField(queryset=Customer.objects.filter(CustomerStatus=True), slug_field='PublicId')
    Employee = SlugRelatedField(queryset=User.objects.filter(EmploymentStatus=True), slug_field='EmployeeId')

    class Meta:
        model = Clearance
        fields = ['id', 'Customer', 'Employee', 'TotalCost', 'TotalPaid', 'Refer', 'Payment', 'Created', 'Updated']
        read_only_field = ['Created','id']

