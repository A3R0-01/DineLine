from django.db import models
from main.abstract.models import AbstractManager, AbstractModel
# Create your models here.
class TableManager(AbstractManager):
    pass

class Table(AbstractModel):
    TableNumber = models.IntegerField(unique=True)
    TableSits = models.IntegerField(default=2)
    TableFee = models.FloatField(default=0.00)
    FuncStatus = models.BooleanField(default=True)
    TableStatus = models.BooleanField(default=False)

    objects = TableManager()

    def __str__(self) -> str:
        return f"{self.TableNumber}: {self.TableFee}"
    
    class Meta:
        db_table = "'main.tables'"