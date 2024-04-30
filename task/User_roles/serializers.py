from rest_framework import serializers
from .models import *

class Userserializers(serializers.ModelSerializer):
    class Meta:
        model=User
        field = "all"

class Roleserializers(serializers.ModelSerializer):
    class Meta:
        model=Role
        field = "all"

class UserRoleserializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ['id', 'User_id', 'Role_id', 'status']