from django.shortcuts import render

# Create your views here.
from .models import UserProfile, Client, UPS, RepairAssignment, RepairUpdate
from .serializers import UserProfileSerializer, ClientSerializer, UPSSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response

class UPSListView(generics.ListAPIView):
    queryset = UPS.objects.all()
    serializer_class = UPSSerializer

class UPSCreateView(generics.CreateAPIView):
    queryset = UPS.objects.all()
    serializer_class = UPSSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)