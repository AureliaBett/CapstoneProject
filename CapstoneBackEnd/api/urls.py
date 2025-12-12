from django.urls import path
from .views import UPSListView, UPSCreateView, UPSDeleteView, UPSUpdateView
from .auth_views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('UPSs/' , UPSListView.as_view(), name='ups-list'),
    path('create-ups/', UPSCreateView.as_view(), name='ups-create'),
    path('update-ups/<int:pk>/', UPSUpdateView.as_view(), name='ups-update'),
    path('delete-ups/<int:pk>/', UPSDeleteView.as_view(), name='ups-delete'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),

]