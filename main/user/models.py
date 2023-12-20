import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
# Create your models here.

class UserManager(BaseUserManager):

    def get_employee_by_id(self, employeeId):
        try:
            instance = self.get(EmployeeId=employeeId)
            return instance
        except(ObjectDoesNotExist, ValueError, TypeError): 
            return Http404
    
    def create_user(self, FirstName, Surname, Salary, Address, Email, NatId, EmployeeAccess=False, password=None, **kwargs):
        if FirstName is None:
            raise TypeError('User must have a First Name')
        if Surname is None:
            raise TypeError('User must have a Surname')
        if Salary is None:
            raise TypeError('User must have a Salary')
        if Address is None:
            raise TypeError('User must have an Address')
        if Email is None:
            raise TypeError('User must have an Email ')
        if NatId is None:
            raise TypeError('User must have a National Id number')
        if password is None:
            raise TypeError('User must have a Password')

        user = self.model(FirstName=FirstName, Surname=Surname, Salary=Salary, EmployeeAccess=EmployeeAccess, Address=Address, Email=self.normalize_email(Email), NatId=NatId)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self, FirstName, Surname, Salary, Address, Email, NatId, password=None, **kwargs):
        if FirstName is None:
            raise TypeError('Superuser must have a First Name')
        if Surname is None:
            raise TypeError('Superuser must have a Surname')
        if Salary is None:
            raise TypeError('Superuser must have a Salary')
        if Address is None:
            raise TypeError('Superuser must have an Address')
        if Email is None:
            raise TypeError('Superuser must have an Email ')
        if NatId is None:
            raise TypeError('Superuser must have a National Id number')
        if password is None:
            raise TypeError('Superuser must have a Password')
        user = self.create_user(FirstName, Surname, Salary, Address, Email, NatId, True, password, **kwargs)
        user.is_superuser = True
        user.save(using=self._db)

class User(AbstractBaseUser, PermissionsMixin):
    EmployeeId = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    FirstName = models.CharField(max_length=40)
    Surname = models.CharField(max_length=40)
    Salary = models.IntegerField()
    Address = models.CharField(max_length=150)
    Email = models.EmailField(db_index=True, unique=True)
    EmploymentStatus = models.BooleanField(default=True)
    EmployeeAccess = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    NatId = models.CharField(max_length=40, unique=True, db_index=True)
    DateAdded = models.DateField(auto_now=True)
    DateLeft = models.DateField(null=True)

    USERNAME_FIELD = 'Email'
    REQUIRED_FIELDS = ['FirstName', 'Surname']
    objects = UserManager()

    def __str__(self) -> str:
        return f"{self.Email}"
    
    class Meta:
        db_table = "'main.user'"
    
    @property
    def name(self):
        return f"{self.FirstName} {self.Surname}"






