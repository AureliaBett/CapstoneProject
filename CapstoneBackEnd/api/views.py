from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import UPS
from .serializers import UPSSerializer
from .permissions import IsManager

# List all UPS units (GET)
class UPSListView(APIView):
    
    def get(self, request):
        ups_units = UPS.objects.all()
        serializer = UPSSerializer(ups_units, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Create a new UPS unit (POST)
class UPSCreateView(APIView):
    permission_classes = [IsAuthenticated, IsManager]
    
    def post(self, request):
        serializer = UPSSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve a single UPS unit (GET)
class UPSDetailView(APIView):
    def get(self, request, pk):
        try:
            ups = UPS.objects.get(pk=pk)
        except UPS.DoesNotExist:
            return Response({"error": "UPS not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UPSSerializer(ups)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Update a UPS unit (PUT)
class UPSUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsManager]
    def put(self, request, pk):
        try:
            ups = UPS.objects.get(pk=pk)
        except UPS.DoesNotExist:
            return Response({"error": "UPS not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UPSSerializer(ups, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete a UPS unit (DELETE)
  
class UPSDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsManager] 
    def delete(self, request, pk):
        try:
            ups = UPS.objects.get(pk=pk)
        except UPS.DoesNotExist:
            return Response({"error": "UPS not found"}, status=status.HTTP_404_NOT_FOUND)

        ups.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
