# Job Portal Management System (Django)

A comprehensive Django REST API for managing job postings and applications where users can apply for jobs, search for specific positions, list all available jobs, and manage their applications.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [API Testing](#api-testing)
- [Known Issues / Future Improvements](#-known-issues--future-improvements)

## ✨ Features

- **Job Management**
  - Create new job postings
  - List all available jobs
  - Search for specific jobs
  - Update job details
  - Delete job postings

- **Application Management**
  - Apply for jobs
  - View all applications
  - View specific application details
  - Delete/withdraw applications

- **Additional Features**
  - Django REST Framework serialization
  - Input validation using DRF validators
  - Comprehensive error handling
  - RESTful API design

## 🛠️ Tech Stack

- **Framework**: Django 5.x
- **API Framework**: Django REST Framework (DRF)
- **Database**: SQLite (development) / PostgreSQL (production)
- **Python Version**: 3.10+
- **Authentication**: Optional JWT (djangorestframework-simplejwt)
- **Testing**: Postman

## 📁 Project Structure

```

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
   cd job-portal-system
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

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
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
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (SQLite is default, uncomment for PostgreSQL)
# DATABASE_URL=postgresql://username:password@localhost:5432/job_portal

# Optional: JWT Settings (if using authentication)
# JWT_SECRET_KEY=your-jwt-secret-key
```

## 📦 Dependencies (requirements.txt)

```txt
Django==5.0.1
djangorestframework==3.14.0
django-filter==23.5
python-decouple==3.8
djangorestframework-simplejwt==5.3.1  # Optional: for JWT auth
psycopg2-binary==2.9.9  # Optional: for PostgreSQL
django-cors-headers==4.3.1
```

## 📡 API Endpoints

### Job Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/jobs/` | Create a new job posting | No |
| GET | `/api/jobs/` | Get all job postings | No |
| GET | `/api/jobs/{id}/` | Get a specific job by ID | No |
| PATCH | `/api/jobs/{id}/` | Update a job posting | No |
| DELETE | `/api/jobs/{id}/` | Delete a job posting | No |
| GET | `/api/jobs/search/?q=` | Search jobs by title/description | No |

### Application Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/applications/apply/{id}/` | Apply for a job | No |
| GET | `/api/applications/` | Get all applications | No |
| GET | `/api/applications/{id}/` | Get a specific application | No |
| DELETE | `/api/applications/{id}/` | Delete/withdraw an application | No |

## 🧪 API Testing

All endpoints have been tested using Postman. Screenshots are available in the `postman/screenshots/` folder.

### Import Postman Collection

1. Open Postman
2. Click Import
3. Select `postman/Job_Portal_Collection.json`
4. Update the base URL if needed (default: `http://127.0.0.1:8000`)

### Sample Test Cases

#### 1. Create a Job
```json
POST /api/jobs/
Content-Type: application/json

{
  "title": "Backend Developer",
  "company": "Tech Corp",
  "location": "Remote",
  "description": "Looking for an experienced backend developer with Django expertise",
  "salary": "8-12 LPA"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "title": "Backend Developer",
  "company": "Tech Corp",
  "location": "Remote",
  "description": "Looking for an experienced backend developer with Django expertise",
  "salary": "₹60,000-₹80,000",
  "status": "open",
  "created_at": "2026-01-15T10:30:00Z",
  "updated_at": "2026-01-15T10:30:00Z"
}
```

#### 2. List All Jobs
```
GET /api/jobs/
```

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "title": "Backend Developer",
    "company": "Tech Corp",
    "location": "Remote",
    "description": "Looking for an experienced backend developer",
    "requirements": "Python, Django, REST APIs",
    "salary": "8-12 LPA",
    "created_at": "2026-01-15T10:30:00Z"
  }
]
```

#### 3. Search for Jobs
```
GET /api/jobs/search/?q=backend
```

#### 4. Apply for a Job
```json
POST /api/applications/apply/{id}/
Content-Type: application/json

{
  "id": 1,
  "applicant_name": "Arhan Khan",
  "email": "khanarhan0205@gmail.com",
  "phone": "+91-9876543210",
  "resume": "https://drive.google.com/file/d/xyz",
  "cover_letter": "I am very interested in this Backend Developer position..."
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "job": 1,
  "applicant_name": "Arhan Khan",
  "email": "khanarhan0205@gmail.com",
  "phone": "+91-9876543210",
  "resume": "https://drive.google.com/file/d/xyz",
  "cover_letter": "I am very interested in this position...",
  "status": "pending",
  "applied_at": "2026-01-15T11:00:00Z"
}
```

#### 5. Get All Applications
```
GET /api/applications/
```

#### 6. Delete an Application
```
DELETE /api/applications/1/
```

**Response (204 No Content)**

## 📸 Postman Screenshots

Check the `postman/screenshots/` folder for:
- `1-create-job.png` - Create Job API
- `2-list-jobs.png` - List All Jobs API
- `3-search-jobs.png` - Search Job API
- `4-apply-job.png` - Apply for Job API
- `5-list-applications.png` - List Applications API
- `6-delete-application.png` - Delete Application API

## 🐛 Known Issues / Future Improvements

- [ ] Implement pagination for job listings
- [ ] Add email notifications for application status
- [ ] Implement file upload for resumes (using Django's FileField)
- [ ] Add advanced search filters with django-filter
- [ ] Add API rate limiting with django-ratelimit
- [ ] Write unit tests using Django TestCase
```

## 📝 Notes

This project was developed as part of the QSkill Backend Development Internship.

**Task Requirement Met**: ✅ Users can apply for a job, search for a particular job, list all available jobs, and delete an application for previously applied jobs.

**Django Version**: 5.0.1  
**DRF Version**: 3.14.0  
**Python Version**: 3.10+
