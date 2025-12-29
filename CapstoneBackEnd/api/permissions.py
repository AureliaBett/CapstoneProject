from rest_framework.permissions import BasePermission

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "manager"
class IsEngineer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "engineer"

class IsTechnician(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "technician"
    
class IsAssignedEngineerOrManager(BasePermission):
    """
    Allow access if user is the assigned engineer or a manager.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.role == "manager":
            return True
        if request.user.role == "engineer" and hasattr(obj, "engineer"):
            return obj.engineer == request.user
        return False