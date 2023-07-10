from django.contrib import admin
from .models import Profile

# Register your  admin models here.
class ProfileAdmin(admin.ModelAdmin):
    pass
#register the profile model so that it would be displayed on the admin page
admin.site.register(Profile , ProfileAdmin)