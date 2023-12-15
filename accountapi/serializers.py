from rest_framework import serializers
from accountapi.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'role', 'email']
        extra_kwargs = {'password': {'write_only': True}}
