from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('applicant', 'Applicant'),
        ('recruiter', 'Recruiter'),
        ('admin', 'Admin'),
    )

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    work_status = models.CharField(
        max_length=20,
        choices = [
            ('experienced', 'Experienced'),
            ('Fresher', 'Fresher'),
        ],
        default='Fresher'
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='applicant')

    def __str__(self):
        return self.username