from django import forms

from .models import Listing

class ListingForm(forms.ModelForm):
    vin = forms.CharField(required=False)
    mileage = forms.CharField(required=False)
    
    class Meta:
        model = Listing
        fields = {'brands', 'model', 'vin' , 'mileage' , 'color' , 'description' , 'engine' ,'transmission' , 'image'}