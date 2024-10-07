from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=30)
    experience_level = models.CharField(max_length=50)
    skills = models.JSONField()  
    preferences = models.JSONField() 
    
    def __str__(self):
        return self.name
