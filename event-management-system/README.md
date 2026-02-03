# Event Management System (Django)

A robust Django REST API platform for creating and managing events with user registration, capacity management, JWT authentication, and admin approval workflows.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [API Testing](#api-testing)
- [Known Issues / Future Improvements](#-known-issues--future-improvements)

## ✨ Features

### Event Management
- Create events with complete details (title, description, date, time, location, capacity)
- View all events
- Filter events by date
- Filter events by location
- Update event details
- Delete events
- Event capacity management

### User Registration
- Register for events
- Validation for event capacity (cannot register if event is full)
- View registered events
- Cancel registration

### Authentication & Authorization
- User authentication using JWT (Simple JWT)
- Role-based access control
- Admin role for event approvals
- Protected routes with permission classes

### Admin Features
- Review and approve/reject events
- Manage all events
- View all registrations
- Admin-only endpoints

## 🛠️ Tech Stack

- **Framework**: Django 5.x
- **API Framework**: Django REST Framework (DRF)
- **Database**: SQLite (development) / PostgreSQL (production)
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Python Version**: 3.10+
- **Testing**: Postman

## 📁 Project Structure

```
event-management-system/
├── manage.py                    # Django management script
├── event_management/            # Django project directory
│   ├── __init__.py
│   ├── settings.py              # Project settings
│   ├── urls.py                  # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── accounts/                       # Custom user app
│   ├── __init__.py
│   ├── models.py                # Custom User model
│   ├── serializers.py           # User serializers
│   ├── views.py                 # Authentication views
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
├── events/                      # Events app (manages events and registrations)
│   ├── __init__.py
│   ├── models.py                # Event and registration models
│   ├── serializers.py           # Event and registration serializers
│   ├── views.py                 # Event viewsets
│   ├── urls.py
│   ├── permissions.py           # Custom permissions
│   ├── admin.py
│   └── migrations/
├── postman/                     # Postman collection & screenshots
│   ├── screenshots/             # Postman API testing screenshots
├── requirements.txt             # Python dependencies
├── .gitignore
└── README.md
```
## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- virtualenv (recommended)

### Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd event-management-system
   ```

2. **Create and activate virtual environment**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser (admin)**
   ```bash
   python manage.py createsuperuser
   # Follow prompts to create admin user
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Server should be running on**
   ```
   http://127.0.0.1:8000/
   ```

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
# Django Settings
SECRET_KEY=your-super-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (SQLite is default, uncomment for PostgreSQL)

# JWT Settings
JWT_SECRET_KEY=your-jwt-secret-key-here
JWT_ACCESS_TOKEN_LIFETIME=60  # minutes
JWT_REFRESH_TOKEN_LIFETIME=1440  # minutes (1 day)
```

## 📦 Dependencies (requirements.txt)

```txt
Django==5.0.1
djangorestframework==3.14.0
djangorestframework-simplejwt==5.3.1
django-filter==23.5
python-decouple==3.8
psycopg2-binary==2.9.9  # Optional: for PostgreSQL
django-cors-headers==4.3.1
```

## 📡 API Endpoints

### Authentication Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/register/` | Register a new user | No |
| POST | `/api/auth/login/` | Login user (get JWT tokens) | No |
| POST | `/api/auth/token/refresh/` | Refresh access token | No |

### Event Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/events/` | Create a new event | Yes |
| GET | `/api/events/` | Get all events | No |
| GET | `/api/events/{id}/` | Get a specific event | No |
| PUT | `/api/events/{id}/` | Update an event | Yes (Owner/Admin) |
| PATCH | `/api/events/{id}/` | Partial update an event | Yes (Owner/Admin) |
| DELETE | `/api/events/{id}/` | Delete an event | Yes (Owner/Admin) |
| GET | `/api/events/?date=` | Filter events by date | No |
| GET | `/api/events/?location=` | Filter events by location | No |

### Registration Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/events/{id}/register/` | Register for an event | Yes |
| GET | `/api/registrations/` | Get user's registrations | Yes |
| GET | `/api/registrations/my/` | Get my registrations | Yes |
| DELETE | `/api/registrations/{id}/cancel/` | Cancel registration | Yes |

### Admin Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/events/admin/pending/` | Get pending events | Yes (Admin) |
| POST | `/api/events/{id}/approve/` | Approve an event | Yes (Admin) |
| POST | `/api/events/{id}/reject/` | Reject an event | Yes (Admin) |
| GET | `/api/registrations/admin/` | Get all registrations | Yes (Admin) |

## 🔒 Authentication

This system uses JWT (JSON Web Tokens) via `djangorestframework-simplejwt`.

### 1. Register a New User
```json
POST /api/auth/register/
Content-Type: application/json

{
    "username": "Alice",
    "password": "qwerty01",
    "email": "alice@example.com",
    "role": "organizer"
}
```

**Response (201 Created):**
```json
{
  "User Registered Successfully"
}
```

### 2. Login (Get JWT Tokens)
```json
POST api/token/
Content-Type: application/json

{
  "username": "arhan",
  "password": "SecurePass123!"
}
```

**Response (200 OK):**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
}
```

### 3. Using JWT Token
Include the access token in the Authorization header:
```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

### 4. Refresh Token
```json
POST api/token/refresh/
Content-Type: application/json

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

## 🧪 API Testing

All endpoints have been tested using Postman. Screenshots are available in the `postman/screenshots/` folder.

### Import Postman Collection

1. Open Postman
2. Click Import
3. Select `postman/Event_Management_Collection.json`
4. Set up environment variables:
   - `base_url`: `http://127.0.0.1:8000`
   - `access_token`: (Will be set after login)

### Sample Test Cases

#### 1. Create an Event
```json
POST /api/events/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "title": "Django Workshop 2026",
  "description": "Learn Django REST Framework from basics to advanced",
  "date": "2026-03-15",
  "time": "14:00:00",
  "location": "Tech Hub, Lucknow",
  "capacity": 50
}
```

**Response (201 Created):**
```json
{
    "id":1,
    "is_approved":false,
    "title":"QSkill Induction",
    "description":"An induction program for internship.",
    "date":"2026-02-15",
    "time":"14:00:00",
    "location":"Lucknow",
    "capacity":150,
    "is_rejected":false,
    "created_by":"Farhan",
    "created_at":"2026-02-02T16:50:08.649341Z"
}
```

#### 2. List All Events
```
GET /api/events/
```

#### 3. Filter Events by Date
```
GET /api/events/?date=2026-03-15
```

#### 4. Filter Events by Location
```
GET /api/events/?location=Lucknow
```

#### 5. Register for an Event
```json
POST /api/events/1/register/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "additional_info": "Looking forward to learning Django!"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "event": 1,
  "user": 1,
  "registered_at": "2026-01-20T11:00:00Z",
  "status": "active",
  "additional_info": "Looking forward to learning Django!"
}
```

**Error if event is full (400 Bad Request):**
```json
{
  "error": "Event is already at full capacity"
}
```

#### 6. Get My Registrations
```
GET /api/registrations/my/
Authorization: Bearer <access_token>
```

#### 7. Cancel Registration
```
DELETE /api/registrations/1/
Authorization: Bearer <access_token>
```

**Response (204 No Content)**

#### 8. Admin Approve Event
```json
POST /api/events/1/approve/
Authorization: Bearer <admin_access_token>
Content-Type: application/json

```

**Response (200 OK):**
```json
{
  "id": 1,
  "title": "Django Workshop 2026",
  "status": "approved",
  "message": "Event approved successfully"
}
```

## 📸 Postman Screenshots

Check the [`postman/screenshots/`](./postman/screenshots/) folder for:

- [`1-register-user.png`](./postman/screenshots/register-user.png) – User Registration  
- [`2-login-user.png`](./postman/screenshots/login-user.png) – User Login (JWT tokens)  
- [`3-create-event.png`](./postman/screenshots/create-event.png) – Create Event  
- [`4-list-events.png`](./postman/screenshots/list-events.png) – List All Events  
- [`5-filter-by-location.png`](./postman/screenshots/filter-by-location.png) – Filter Events by Location  
- [`6-register-event.png`](./postman/screenshots/register-event.png) – Register for Event  
- [`7-my-registrations.png`](./postman/screenshots/my-registrations.png) – Get My Registrations  
- [`8-cancel-registration.png`](./postman/screenshots/cancel-registration.png) – Cancel Registration  
- [`9-admin-approve.png`](./postman/screenshots/admin-approve.png) – Admin Approve Event  
- [`10-capacity-full-error.png`](./postman/screenshots/capacity-full-error.png) – Capacity Validation Error

## 🐛 Known Issues / Future Improvements

- [ ] Add email notifications for event reminders
- [ ] Implement pagination for events list
- [ ] Add event categories/tags with many-to-many relationship
- [ ] QR code generation for event tickets
- [ ] Export events to iCal format
- [ ] Waiting list for full events
- [ ] Event reviews and ratings
- [ ] Write comprehensive unit tests
- [ ] Add Celery for background tasks (email sending)

**Task Requirements Met**: 
✅ Users can create and manage events (title, description, date, time, location, capacity)  
✅ Other users can register for events with capacity validation  
✅ View all events, filter by date/location, and cancel registrations  
✅ User authentication using JWT and admin roles for event approvals  

**Django Version**: 5.0.1  
**DRF Version**: 3.14.0  
**Simple JWT Version**: 5.3.1  
**Python Version**: 3.10+
