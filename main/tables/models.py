from django.db import models
from main.abstract.models import AbstractManager, AbstractModel
# Create your models here.
class TableManager(AbstractManager):
    def clear_table(self, PublicId):
        if PublicId is None:
            raise TypeError('Table must have an Id')
        table = self.get(PublicId = PublicId)
        table.TableStatus = False
        table.save()
    def occupy_table(self, PublicId):
        if PublicId is None:
            raise TypeError('Table must have an Id')
        table = self.get(PublicId = PublicId)
        table.TableStatus = True
        table.save()
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