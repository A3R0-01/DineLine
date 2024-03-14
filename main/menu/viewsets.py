from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .serializer import MenuSerializer
from main.abstract.viewsets import AbstractViewset
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ViewSet
from .models import Menu
from rest_framework.exceptions import ValidationError
from rest_framework.status import HTTP_201_CREATED,HTTP_302_FOUND
from rest_framework.response import Response
# Create your views here.
class MenuViewSet(AbstractViewset):
    http_method_names = ('post', 'patch', 'get',)
    permission_classes = (IsAuthenticated,)
    serializer_class = MenuSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Menu.objects.all()
        elif self.request.user.EmployeeAccess:
            return Menu.objects.exclude(FuncStatus=False)
        else:
            return Menu.objects.exclude(FoodStatus=False)
    
    def get_object(self):
        obj = Menu.objects.get_by_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def create(self, request, *args, **kwargs):
        if self.request.user.EmployeeAccess or self.request.user.is_superuser:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=HTTP_201_CREATED)
        else: raise ValidationError('You Are Not authorized to create a Menu Item')

