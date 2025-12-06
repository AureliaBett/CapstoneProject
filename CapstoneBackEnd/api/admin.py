from django.contrib import admin
from .models import Client,Branch, UPS

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contract', 'contact_email')
    search_fields = ('name', 'contact_email')

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'location')
    search_fields = ('client__name', 'location')
    autocomplete_fields = ('client',)

@admin.register(UPS)
class UPSAdmin(admin.ModelAdmin):
    list_display = ('id', 'branch', 'serial_number', 'model', 'status', 'received_date')
    search_fields = ('serial_number', 'model', 'branch__client__name', 'branch__location')
    list_filter = ('status', 'received_date')
    autocomplete_fields = ('branch',)  # Allows search dropdown for branch