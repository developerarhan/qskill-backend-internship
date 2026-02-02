# QSkill Backend Development Internship

This repository contains my submissions for the QSkill Backend Development Internship.

## 📋 Internship Details

- **Domain**: Backend Development Django
- **Duration**: 10th January 2026 - 10th February 2026
- **Tasks Completed**: 2/2

## 🗂️ Repository Structure

```
qskill-backend-internship/
├── job-portal-system/          # Task 1: Job Portal Management System
│   ├── README.md              # Detailed documentation for Job Portal
│   ├── manage.py              # Django management script
│   ├── job_portal/            # Django project directory
│   ├── jobs/                  # Jobs app
│   ├── applications/          # Applications app
│   └── requirements.txt       # Python dependencies
│
├── event-management-system/    # Task 2: Event Management System
│   ├── README.md              # Detailed documentation for Event Management
│   ├── manage.py              # Django management script
│   ├── event_management/      # Django project directory
│   ├── accounts/              #  Accounts app (authentication)
│   ├── events/                # Events app 
│   └── requirements.txt       # Python dependencies
│
└── README.md                   # This file (main overview)
```

## 📁 Projects Overview

### 1. Job Portal Management System
A comprehensive Django REST API for managing job postings and applications.

**Key Features:**
- Create and manage job postings
- Search and filter jobs
- Apply for jobs
- Manage applications
- Delete applications

**Tech Stack:** Python 3.x, Django 5.x, Django REST Framework, SQLite

[📖 View Detailed Documentation](./job-portal-system/README.md)

---

### 2. Event Management System
A robust Django backend platform for creating and managing events with user registration.

**Key Features:**
- Create and manage events (title, description, date, time, location, capacity)
- User registration for events with capacity validation
- Filter events by date/location
- Cancel registrations
- JWT authentication using Simple JWT
- Admin roles for event approvals

**Tech Stack:** Python 3.x, Django 5.x, Django REST Framework, Simple JWT, SQLite

[📖 View Detailed Documentation](./event-management-system/README.md)

---

## 🚀 Quick Start

Each project has its own setup instructions. Navigate to the respective project folders and follow their README files:

```bash
# For Job Portal System
cd job-portal-system
# Follow instructions in job-portal-system/README.md

# For Event Management System
cd event-management-system
# Follow instructions in event-management-system/README.md
```

## 📸 API Testing

All APIs have been thoroughly tested using Postman. Screenshots and collections are available in each project's README.md .

## 🛠️ Technologies Used

- **Backend Framework**: Django 5.x
- **API Framework**: Django REST Framework (DRF)
- **Database**: SQLite (development)
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Python Version**: 3.10+
- **Testing Tool**: Postman
- **Version Control**: Git & GitHub

## 📝 Task Requirements Met

### Job Portal Management System ✅
- [x] User can apply for a job
- [x] User can search for a specific job
- [x] User can list all available jobs
- [x] User can delete an application for previously applied job

### Event Management System ✅
- [x] Users can create and manage events (title, description, date, time, location, capacity)
- [x] Other users can register for events (with capacity validation)
- [x] View all events, filter by date/location
- [x] Cancel registrations
- [x] User authentication and admin roles for event approvals

## 📧 Contact

**Name**: Arhan Khan  
**Email**: khanarhan0205@gmail.com  

---

## 📄 License

This project is created for educational purposes as part of the QSkill Internship program.

---
