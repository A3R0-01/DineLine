from rest_framework import serializers
from main.user.models import User

class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='EmployeeId', read_only=True, format="hex")
    DateAdded = serializers.DateField(read_only=True)
    DateLeft = serializers.DateField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'FirstName', 'Surname', 'Salary', 'Address', 'Email', 'EmploymentStatus', 'EmployeeAccess', 'is_active', 'NatId', 'DateAdded', 'DateLeft' ]
        read_only_field = ['is_active']