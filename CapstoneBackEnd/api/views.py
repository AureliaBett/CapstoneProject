from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import UPS, RepairAssignment, RepairUpdate
from .serializers import UPSSerializer, RepairAssignmentSerializer, RepairUpdateSerializer
from .permissions import IsManager

# List all UPS units (GET)
class UPSListView(APIView):
    permission_classes = [IsAuthenticated]  
   
    def get(self, request):
        ups_units = UPS.objects.all()

        # ---------------------
        # Query params for filtering/search
        # ---------------------
        status_param = request.query_params.get("status")
        branch = request.query_params.get("branch")
        client_name = request.query_params.get("client")
        model_search = request.query_params.get("model")
        serial_search = request.query_params.get("serial")

        if status_param:
            ups_units = ups_units.filter(status__iexact=status_param)
        if branch:
            ups_units = ups_units.filter(branch__icontains=branch)
        if client_name:
            ups_units = ups_units.filter(client__name__icontains=client_name)
        if model_search:
            ups_units = ups_units.filter(model__icontains=model_search)
        if serial_search:
            ups_units = ups_units.filter(serial_number__icontains=serial_search)

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
    
# Assign a UPS to an engineer
class RepairAssignmentCreateView(APIView):
    permission_classes = [IsAuthenticated, IsManager]

    def post(self, request):
        serializer = RepairAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# List all assignments (or filter by engineer)
class RepairAssignmentListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.role == "manager":
            assignments = RepairAssignment.objects.all()
        else:  # engineer or technician sees only their assignments
            assignments = RepairAssignment.objects.filter(engineer=user)
        serializer = RepairAssignmentSerializer(assignments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Add a repair update to an assignment
class RepairUpdateCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Check if engineer is assigned to this assignment
        assignment_id = request.data.get("assignment")
        try:
            assignment = RepairAssignment.objects.get(id=assignment_id)
        except RepairAssignment.DoesNotExist:
            return Response({"error": "Assignment not found"}, status=status.HTTP_404_NOT_FOUND)

        if request.user.role != "manager" and request.user != assignment.engineer:
            return Response({"error": "You are not allowed to add updates to this assignment"}, status=status.HTTP_403_FORBIDDEN)

        serializer = RepairUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# List updates for a specific assignment
class RepairUpdateListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, assignment_id):
        try:
            assignment = RepairAssignment.objects.get(id=assignment_id)
        except RepairAssignment.DoesNotExist:
            return Response({"error": "Assignment not found"}, status=status.HTTP_404_NOT_FOUND)

        user = request.user
        if user.role == "manager" or user == assignment.engineer:
            updates = RepairUpdate.objects.filter(assignment=assignment)
        else:
            updates = RepairUpdate.objects.none()  # Technicians see none by default
        serializer = RepairUpdateSerializer(updates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)