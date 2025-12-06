from rest_framework import serializers
from .models import UserProfile, Client, UPS
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['user', 'role']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class UPSSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = UPS
        fields = '__all__'