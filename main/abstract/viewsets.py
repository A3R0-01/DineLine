from rest_framework import viewsets
from rest_framework import filters

class AbstractViewset(viewsets.ModelViewSet):
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['Updated', 'Created']
    ordering = ['-Created']
