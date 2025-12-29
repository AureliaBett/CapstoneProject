from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    ROLES = (
        ('manager', 'Workshop Manager'),
        ('engineer', 'Bench Engineer'),
        ('technician', 'Field Technician'), 
    )
   
    
    role = models.CharField( max_length=20,  choices=ROLES, default='technician', )
    work_phone = models.CharField(max_length=15, blank=True, null=True, default="")
    

    def __str__(self):
        return f"{self.username} ({self.role})"


class Client(models.Model):
    name = models.CharField(max_length=100)
    contract = models.CharField(max_length=100, default="Satisfactory")
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
   
    def __str__(self):
        return self.name




class UPS(models.Model):
    STATUS = (
        ('received', 'Received'),
        ('diagnosis', 'Diagnosis'),
        ('repairing', 'Repairing'),
        ('completed', 'Completed'),
        ('released', 'Released'),
    )

    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="ups_units")
    branch = models.CharField(max_length=120)
    status = models.CharField(max_length=20, choices=STATUS, default='received')
    received_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.model} - {self.serial_number}"


class RepairAssignment(models.Model):
    ups = models.ForeignKey(UPS, on_delete=models.CASCADE, related_name="assignments")
    engineer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assigned_repairs"
    )
    assigned_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Assignment: {self.ups.serial_number} → {self.engineer.username}"


class RepairUpdate(models.Model):
    assignment = models.ForeignKey(RepairAssignment, on_delete=models.CASCADE, related_name="updates")
    notes = models.TextField()
    attached_file = models.FileField(upload_to="repair_files/", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Update for {self.assignment.ups.serial_number}"
