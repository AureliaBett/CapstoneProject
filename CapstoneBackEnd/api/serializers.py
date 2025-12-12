from rest_framework import serializers
from .models import Client, UPS, CustomUser



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', "password", 'role']



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'



class UPSSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = UPS
        fields = '__all__'

    def create(self, validated_data):
        # Extract nested data
        client_data = validated_data.pop('client')
        
        # Either get existing client or create new
        client, _ = Client.objects.get_or_create(**client_data)
        # Either get existing branch or create new under this client
        

        # Create the UPS with the associated client and branch
        ups = UPS.objects.create(client=client,  **validated_data)
        return ups