from django.db import models

# Create your models here.

class JobProfile(models.Model):
    job_id = models.IntegerField(primary_key=True)
    job_title = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    required_skills = models.JSONField()
    location = models.CharField(max_length=30)
    job_type = models.CharField(max_length=30)
    experience_level = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"job_id={self.job_id},title={self.job_title}"

