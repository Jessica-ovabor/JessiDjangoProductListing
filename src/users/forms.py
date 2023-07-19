from dtatclasses import field
from django import forms 
from localflavor.us.forms import  USZipCodeField
from  .models import Location

class LocationForm(forms.ModelForm):
    address_1 = forms.CharField(required=True)
    zip_code = USZipCodeField(required=True)
    class Meta:
        model =Location
        fields ={'address_1' , 'address_2' , 'city' , 'state' , 'zip_code', }