from django.db import models, transaction
from main.abstract.models import AbstractModel, AbstractManager
from main.orders.models import Order
from main.tables.models import Table

# Create your models here.

class CustomerManager(AbstractManager):
    @transaction.atomic
    def clear_customer(self,PublicId):
        if PublicId is None:
            raise TypeError('Customer must have an Id')
        customer = self.get(PublicId=PublicId)
        customer.CustomerStatus = False
        table = customer.TableId
        table.TableStatus = False
        customer.order_set.exclude(OrderStatus=True).update(FuncStatus=False)
        table.save()
        customer.save()
    pass


class Customer(AbstractModel):
    CustomerName = models.CharField(max_length=100)
    CustomerStatus = models.BooleanField(default=True)
    TableId = models.ForeignKey(to='tables.Table', on_delete=models.PROTECT)

    objects = CustomerManager()

    def __str__(self) -> str:
        return f'Name:\t{self.CustomerName}, Table: {self.TableId.TableNumber}'
    
    class Meta:
        db_table = "'main.customer'"