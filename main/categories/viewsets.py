from django.shortcuts import render
from main.abstract.viewsets import AbstractViewset
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Category
from .serializers import CategoriesSerializer

# Create your views here.
class CategoryViewset(AbstractViewset):
    http_method_names = ('post', 'get', 'patch',)
    permission_classes = (IsAuthenticated,)
    serializer_class = CategoriesSerializer

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.EmployeeAccess:
            return Category.objects.all()
        else:
            return Category.objects.exclude(FuncStatus=False)
    
    def get_object(self):
        obj = Category.objects.get_by_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def create(self, request, *args, **kwargs):
        if self.request.user.EmployeeAccess or self.request.user.is_superuser:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=HTTP_201_CREATED)
        else: raise ValidationError('You Are Not authorized to create a Category')


