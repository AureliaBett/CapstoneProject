from django.urls import path
from .views import UPSListView, UPSCreateView, UPSDeleteView, UPSUpdateView, RepairAssignmentCreateView, RepairUpdateCreateView,RepairAssignmentListView,RepairUpdateListView 
from .auth_views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('UPSs/' , UPSListView.as_view(), name='ups-list'),
    path('create-ups/', UPSCreateView.as_view(), name='ups-create'),
    path('update-ups/<int:pk>/', UPSUpdateView.as_view(), name='ups-update'),
    path('delete-ups/<int:pk>/', UPSDeleteView.as_view(), name='ups-delete'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('assignments/', RepairAssignmentListView.as_view(), name='assignment-list'),
    path('assignments/create/', RepairAssignmentCreateView.as_view(), name='assignment-create'),
    path('updates/', RepairUpdateCreateView.as_view(), name='update-create'),
    path('updates/<int:assignment_id>/', RepairUpdateListView.as_view(), name='update-list'),

]