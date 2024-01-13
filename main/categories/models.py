from django.db import models
from main.abstract.models import AbstractModel
from main.abstract.models import AbstractManager
from rest_framework.exceptions import ValidationError
# Create your models here.
class CategoryManager(AbstractManager):
    def create(self, CategoryName, **kwargs):
        if CategoryName is None:
            raise TypeError("Category should have a name")
        if self.filter(CategoryName=CategoryName, FuncStatus=True).exists():
            raise ValidationError('Category Exists')
        else:
            category = self.model(CategoryName=CategoryName)
            category.save()
            return category

    pass
class Category(AbstractModel):
    CategoryName = models.CharField(max_length=30, null=False)
    FuncStatus = models.BooleanField(default=True)

    objects = CategoryManager()

    def __str__(self) -> str:
        return f'{self.CategoryName}: {self.FuncStatus}'
    
    class Meta:
        db_table = 'main.categories'