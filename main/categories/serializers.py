from main.abstract.serializer import AbstractSerializer
from main.menu.serializer import MenuSerializer
from .models import Category

class CategoriesSerializer(AbstractSerializer):

    class Meta:
        model = Category
        fields = ['id', 'CategoryName', 'FuncStatus', 'Created', 'Updated']
        read_only_fields = ['Created', 'id']
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        cat = Category.objects.get_by_id(rep['id'])
        menuItems = cat.menu_set.filter(FuncStatus=True, FoodStatus=True).count()
        outOfOrder = cat.menu_set.filter(FuncStatus=True, FoodStatus=False).count()
        rep['Stock'] = menuItems
        rep['OutOfOrder'] = outOfOrder
        return rep

class SingleMenuSerializer(AbstractSerializer):
    class Meta:
        model = Category
        fields = ['id', 'CategoryName', 'FuncStatus']
        read_only_fields = ['Created', 'id']
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        cat = Category.objects.get_by_id(rep['id'])
        menuItems = cat.menu_set.filter(FuncStatus=True)
        rep['MenuItems'] = [MenuSerializer(record).data for record in menuItems]
        return rep
