from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    role_choices=[
        ('Admin','Admin'),
        ('Manager','Manager'),
        ('Employee','Employee')
    ]
    role=models.CharField(max_length=20,choices=role_choices)
    profile_picture=models.ImageField(upload_to='media/profile_picture')
    
class Project(models.Model):
    project_name=models.CharField(max_length=50)
    project_image=models.ImageField(upload_to='media/project_images')
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['project_name',], name='unique_project')
        ]
    def __str__(self):
        return self.project_name