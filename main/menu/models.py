from django.db import models
from main.abstract.models import AbstractManager, AbstractModel
from main.categories.models import Category
from rest_framework.exceptions import ValidationError

# Create your models here.
class MenuManager(AbstractManager):
    def get_by_category(self, public_id):
        category = Category.objects.get(PublicId=public_id)
        return category.menu_set.all()
    pass

class Menu(AbstractModel):
    FoodName = models.CharField(max_length=50)
    CategoryId = models.ForeignKey(to='categories.Category', on_delete=models.PROTECT)
    FoodPrice = models.FloatField(default=5.0)
    FoodDescription = models.CharField(max_length=200)
    FoodStatus = models.BooleanField(default=True)
    FuncStatus = models.BooleanField(default=True)

    objects = MenuManager()
    def __str__(self) -> str:
        return f'{self.FoodName}: {self.FoodPrice}'

    class Meta:
        db_table = 'main.menu'

