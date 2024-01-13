from typing import Any
from django.db import models
from main.abstract.models import AbstractManager, AbstractModel
from rest_framework.exceptions import ValidationError

# Create your models here.
class OrderManager(AbstractManager):

    def create(self, **kwargs: Any) -> Any:
        if self.filter(Customer=kwargs['Customer'].PublicId, OrderStatus=None).exists():
            raise ValidationError("You are not Allowed to Create a new order until the current one is ordered")
        else:
            return super().create(**kwargs)
    pass


class Order(AbstractModel):
    Customer = models.ForeignKey(to='main_customers.Customer', on_delete=models.PROTECT)
    Employee = models.ForeignKey(to='user.User', on_delete=models.PROTECT, null=True)
    OrderStatus = models.BooleanField(default=None, null=True)
    FuncStatus = models.BooleanField(default=True)

    objects = OrderManager()

    def __str__(self) -> str:
        return f'{self.Customer.CustomerName}: {self.Employee.FirstName}: {self.OrderStatus} '
    
    class Meta:
        db_table = 'main.order'