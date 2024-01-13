from main.abstract.viewsets import AbstractViewset
from rest_framework.permissions import IsAuthenticated
from main.customers.models import Customer
from main.customers.serializers import RegisterCustomerSerializer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.status import HTTP_201_CREATED
from main.tables.models import Table

# Create your views here.
class CustomerViewset(AbstractViewset):
    http_method_names = ('post', 'get')
    permission_classes = (IsAuthenticated,)
    serializer_class = RegisterCustomerSerializer

    def get_queryset(self):
        return Customer.objects.all()
    
    def get_object(self):
        obj = Customer.objects.get_by_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)

        return obj
    
    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=HTTP_201_CREATED)
    

