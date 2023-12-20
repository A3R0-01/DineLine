from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from main.user.serializers import UserSerializer
from main.user.models import User
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['patch', 'get']
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)
    
    def get_object(self):
        obj = User.objects.get_employee_by_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj




