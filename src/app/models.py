import uuid
from django.db import models
from users.models import Location, Profile
from .consts import PRODUCTS_BRANDS, TRANSMISSION_OPTIONS, BODY_TYPE,SELLER_TYPE
from .utils import user_listing_path

# Create your models here.
class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    model = models.CharField( max_length=64)
    vin =models.CharField(max_length=17, blank=True)
    brands = models.CharField(max_length=24 , choices=PRODUCTS_BRANDS, default=None)
    mileage = models.IntegerField(default=0)
    color = models.CharField(max_length=24)
    description= models.TextField()
    engine =models.CharField(max_length=24, blank=True)
    transmission=  models.CharField(max_length=24, choices =TRANSMISSION_OPTIONS ,default=None)
    location =models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
    seller_type =models.CharField(max_length=24, choices=SELLER_TYPE)
    body_type = models.CharField(max_length=24 , choices=BODY_TYPE)
    image = models.ImageField(upload_to=user_listing_path)
    
    def __str__(self):
        return f"{self.seller.user.username}\'s Listing - {self.model}"
