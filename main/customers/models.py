from django.db import models
from main.abstract.models import AbstractModel, AbstractManager

# Create your models here.

class CustomerManager(AbstractManager):
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