from django.db import models
from django.contrib.auth.models import User

# Create your profile models: A user can only have one profile.
# After creating your database python manage.py makemigrations and apply migrations
# Install pillow to use image
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)#Cascade deletes the corresponding profile to a user
    photo = models.ImageField(null=True)
    bio = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    # return a user profile with their specific username
    def __str__(self):
        return f"{self.user.username}\'s Profile"
        
    
