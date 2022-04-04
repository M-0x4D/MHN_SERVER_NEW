from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User

from authen_app.models import HackerData, HakcerData3 , HakcerData4

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user




class Data_serializer(serializers.ModelSerializer):
    class Meta:
        model = HakcerData4
        fields = '__all__'