from main.abstract.serializer import AbstractSerializer
from .models import Category

class CategoriesSerializer(AbstractSerializer):

    class Meta:
        model = Category
        fields = ['id', 'CategoryName', 'FuncStatus', 'Created', 'Updated']
        read_only_fields = ['Created', 'id']

