from main.abstract.serializer import AbstractSerializer
from rest_framework.serializers import SlugRelatedField
from main.customers.models import Customer
from main.user.models import User
from .models import Order
from main.foodorders.models import FoodOrder
from main.foodorders.serializers import FoodOrdersSerializers

class OrdersMainSerializer(AbstractSerializer):
    Customer = SlugRelatedField(queryset=Customer.objects.all(), slug_field='PublicId')
    Employee = SlugRelatedField(queryset=User.objects.all(), slug_field='EmployeeId')

    class Meta:
        model = Order
        fields=['id','Customer','Employee','OrderStatus', 'FuncStatus']
        read_only_field = ['Created', 'Updated']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        order = Order.objects.get_by_id(rep['id'])
        foodOrders_per_order = order.foodorder_set.filter(Status=True)
        rep['FoodOrders'] = [FoodOrdersSerializers(i).data for i in foodOrders_per_order]
        return rep