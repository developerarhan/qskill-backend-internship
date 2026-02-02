from django.db import models
from django.conf import settings

from jobs.models import Job

# Create your models here.

class Application(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="applications"
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
         related_name="applications"
    )
    applicant_name = models.CharField(max_length=255, default="Unknown")
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    resume = models.URLField()
    cover_letter = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # One user can apply only once per job
        unique_together = ('user', 'job')

    def __str__(self):
        return f"{self.user} -> {self.job}"