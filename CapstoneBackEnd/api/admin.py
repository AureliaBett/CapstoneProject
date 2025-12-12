from django.contrib import admin
from .models import Client, UPS

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contract', 'contact_email')
    search_fields = ('name', 'contact_email')


@admin.register(UPS)
class UPSAdmin(admin.ModelAdmin):
    list_display = ('id', 'branch', 'serial_number', 'model', 'status', 'received_date')
    search_fields = ('serial_number', 'model', 'branch__client__name', 'branch__location')
    list_filter = ('status', 'received_date')
   