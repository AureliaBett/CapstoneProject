# UninterrUp Frontend

UninterrUp is a modern web-based frontend interface designed for the UPS maintenance and workshop management system. The application allows workshop managers, bench engineers, and field technicians to interact with UPS repair workflows using a clean and intuitive experience.

This frontend consumes a Django REST API backend and provides a full-stack experience through reactive UI and real-time status visibility.

## Key Functionalities
### User Authentication

Secure login

Role-based access

Protected routes

Personalized dashboard

### UPS Management Dashboard

View all UPS units currently in the workshop

Filter by status (received, diagnosis, repairing, completed, released)

View assignment to engineers

Detailed UPS profile view

### Repair Workflows (Engineers)

Accept and work on assigned UPS units

Upload repair notes & attachments

Update current state (diagnosis, repairing, complete)

Generate downloadable reports

### Workshop Manager Tools

Register UPS on arrival

Assign units to engineers

Monitor diagnostics and repair progress

Release units after completion

### File Upload & Downloads

Upload manuals

Upload circuit diagrams

Export repair reports

## Technology Stack
Layer	Technology
Framework	React.js
Styling	Tailwind CSS
HTTP	Axios
State	React Hooks
Routing	React Router
Auth	JWT (via backend API)

## Goals of the Frontend

Provide a user-friendly interface for UPS tracking

Replace manual paper-based workshop processes

Standardize tracking and diagnosis documentation

Help management track repair operations at a glance