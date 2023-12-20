from rest_framework import serializers
from main.user.serializers import UserSerializer
from main.user.models import User

class RegisterSerializer(UserSerializer):
    """
    Registration Serializer for requests and user creation
    """

    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'FirstName', 'Surname', 'Salary', 'Address', 'Email', 'EmployeeAccess', 'NatId', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)