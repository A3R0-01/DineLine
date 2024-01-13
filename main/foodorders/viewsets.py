from main.abstract.viewsets import AbstractViewset
from rest_framework.exceptions import ValidationError, NotAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from main.foodorders.serializers import FoodOrdersSerializers
from rest_framework.status import HTTP_201_CREATED
from main.orders.models import Order
from main.customers.models import Customer
from main.user.models import User
from main.clearance.models import Clearance
from .models import FoodOrder
from django.db import transaction



# Create your views here.
class FoodOrderCreateViewSet(AbstractViewset):
    permission_classes = (IsAuthenticated,)
    http_method_names = ('post','patch', 'delete','get')
    serializer_class = FoodOrdersSerializers

    def get_queryset(self):
        if self.request.user.is_superuser :
            return FoodOrder.objects.all()
        else:
            raise NotAuthenticated('You are not Authorised')

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        customer = Customer.objects.get_by_id(request.data['Customer'])
        del request.data['Customer']
        if  customer.order_set.filter(OrderStatus=None).exists():
            order = customer.order_set.get(OrderStatus=None)
        else:
            employee = self.request.user.EmployeeId
            employee_obj = User.objects.get_employee_by_id(employee)
            order = Order.objects.create(Customer=customer, Employee=employee_obj)
        request.data['Order'] = order.PublicId
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=HTTP_201_CREATED)


