from typing import Any
from django.db import models, transaction
from main.abstract.models import AbstractManager, AbstractModel
from main.orders.models import Order
from main.user.models import User
from main.customers.models import Customer

# Create your models here.
class FoodOrderManager(AbstractManager):

    pass
class FoodOrder(AbstractModel):
    MenuItem = models.ForeignKey(to='menu.Menu', on_delete=models.PROTECT)
    Order = models.ForeignKey(to='orders.Order', on_delete=models.PROTECT)
    Quantity = models.IntegerField(default=1)
    Specification = models.CharField(max_length=200, default=None)
    Status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.MenuItem.FoodName} x{self.Quantity}: {self.Specification}'
    
    class Meta:
        db_table = 'main.foodOrders'
