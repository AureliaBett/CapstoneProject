# uninterrUp (UPS Management and Tracking System)

uninterrUp is a bakcend powered system designed to help workshop teams manage, track and document the repair lifecycle of UPSs from the minute they are received in the workshop to when they are returned to the client/
## Project Overview
This project is a Django REST Framework–based backend API for managing Uninterruptible Power Supply (UPS) units and their repair workflows. It supports role-based access control, authentication, UPS lifecycle management, repair assignments, and repair updates.
## 06/11/2025
Set up of django and djangoframeworks, Created models in models.py, a database in postgresql, performed migrations.
## Tech Stack
-  Python 3
-  Django 5.2
-  Django REST Framework
-  PostgreSQL
-  Token Authentication
-  Gunicorn
-  Render
## Core Features
-  Custom User model with roles (Manager, Engineer, Technician)
-  Token-based authentication
-  UPS CRUD operations
-  Repair assignments
-  Repair updates
-  Search and filtering
## Authentication
-  Uses DRF Token Authentication.
- Authorization Header:
- Authorization: Bearer <token>
## Deployment
-  Deployed on Render using Gunicorn.
-  Procfile command:
- web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn uninterrup.wsgi:application
## Status
-  Backend implementation complete and production-ready.
