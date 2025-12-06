from django.urls import path
from .views import (UPSListView, UPSCreateView)
urlpatterns = [
    path('api/' , UPSListView.as_view(), name='ups-list'),
    path('api/create-ups/', UPSCreateView.as_view(), name='ups-create'),
]