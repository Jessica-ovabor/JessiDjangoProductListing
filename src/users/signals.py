from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Profile,Location
#automate user profile creation
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created , **kwargs):
    if created:
        Profile.objects.create(user=instance)
#automate user profile  location creation
@receiver(post_save, sender=Profile)
def create_profile_location(sender, instance, created , **kwargs):
    if created:
        profile_location = Location.objects.create()
        instance.location=profile_location
        instance.save()
#Delete user location as as soon as the profile is deleted
@receiver(post_delete, sender=Profile)
def delete_profile_location(sender, instance, *args, **kwargs):
    if  instance.location !=None:
        instance.location.delete()