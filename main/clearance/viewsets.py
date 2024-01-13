from main.abstract.viewsets import AbstractViewset
from main.clearance.serializers import ClearanceSerializer
from main.customers.models import Customer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_302_FOUND
from rest_framework.permissions import IsAuthenticated
from .models import Clearance
# Create your views here.

class ClearanceViewSet(AbstractViewset):
    permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch')
    serializer_class = ClearanceSerializer

    def get_queryset(self):
        return Clearance.objects.all()
    
    def get_object(self):
        totalCost = Clearance.objects.update_total_cost(self.kwargs['pk'])
        customer_instance = Customer.objects.get_by_id(self.kwargs['pk'])
        obj = Clearance.objects.get(Customer=customer_instance)
        self.check_object_permissions(self.request, obj)
        return obj
    
class ClearanceOneViewSet(AbstractViewset):
    permission_classes = (IsAuthenticated,)
    http_method_names = ('get',)
    serializer_class = ClearanceSerializer

    def get_object(self):
        obj = Customer.objects.get(self.kwargs['pk'])
        clearance_instance = Clearance.objects.get(Customer=obj)
        self.check_object_permissions(self.request, clearance_instance)
        return clearance_instance
