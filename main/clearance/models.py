from django.db import models, transaction
from main.abstract.models import AbstractManager, AbstractModel
from main.customers.models import Customer
from main.orders.models import Order
from main.foodorders.models import FoodOrder


# Create your models here.
class ClearanceManager(AbstractManager):
    @transaction.atomic
    def update_total_cost(self, customer):
        customer_instance = Customer.objects.get_by_id(customer)
        diction = customer_instance.order_set.filter(OrderStatus=True).annotate(total=models.F('foodorder__Quantity')*models.F('foodorder__MenuItem__FoodPrice')).aggregate(TotalCost=models.Sum('total', default=0))
        TotalCost = diction['TotalCost']
        clearance_instance = self.get(Customer=customer_instance)
        clearance_instance.TotalCost = TotalCost
        clearance_instance.save()
        return TotalCost

    pass


class Clearance(AbstractModel):
    Customer = models.ForeignKey(to='main_customers.Customer', on_delete=models.PROTECT)
    Employee = models.ForeignKey(to='user.User', on_delete=models.PROTECT)
    TotalCost = models.FloatField(default=0)
    TotalPaid = models.FloatField(default=0)
    Payment = models.BooleanField(default=None, null=True)
    Refer = models.BooleanField(default=False)

    objects = ClearanceManager()

    def __str__(self) -> str:
        return f'Totalcost: {self.TotalCost}, Paid: {self.TotalPaid}'

