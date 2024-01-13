from django.shortcuts import render
from main.abstract.viewsets import AbstractViewset
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotAuthenticated
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_302_FOUND
from main.customers.models import Customer
from .serializers import OrdersMainSerializer
from .models import Order

# Create your views here.
class OrdersMainViewSet(AbstractViewset):
    permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch')
    serializer_class = OrdersMainSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Order.objects.all()
        elif self.request.user.EmployeeAccess:
            return Order.objects.filter(FuncStatus=True)
        else:
            raise NotAuthenticated("You Are Not Allowed To Access this Info")
    def get_object(self):
        obj = Order.objects.get_by_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

