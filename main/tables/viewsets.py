from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet
from main.tables.models import Table
from main.tables.serializers import TableSerializer, RegisterTableSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class TableViewSet(ModelViewSet):
    serializer_class = TableSerializer
    http_method_names = ['get', 'patch']
    permission_classes = (AllowAny,)

    def get_object(self):
        obj =  Table.objects.get_by_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        # if self.request.user.EmployeeAccess:
        #     return Table.objects.all()
        return Table.objects.exclude(FuncStatus=False)

class RegisterTableViewSet(ViewSet):
    serializer_class = RegisterTableSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post',]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        table = serializer.save()

        return Response({
            "Table": serializer.data,
        }, status=status.HTTP_201_CREATED)