from main.abstract.serializer import AbstractSerializer
from rest_framework.serializers import SlugRelatedField
from main.foodorders.models import FoodOrder
from main.menu.models import Menu
from main.menu.serializer import MenuSerializer
from main.orders.models import Order

class FoodOrdersSerializers(AbstractSerializer):
    MenuItem = SlugRelatedField(queryset=Menu.objects.exclude(FuncStatus=False, FoodStatus=False), slug_field='PublicId')
    Order = SlugRelatedField(queryset=Order.objects.filter(FuncStatus=True), slug_field='PublicId')
    class Meta:
        model = FoodOrder
        fields = ('id','MenuItem', 'Quantity', 'Order', 'Specification', 'Status','Created', 'Updated')
        read_only_field = ('Created')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        menuitem = Menu.objects.get_by_id(rep['MenuItem'])
        rep['MenuItem'] = MenuSerializer(menuitem).data
        return rep

