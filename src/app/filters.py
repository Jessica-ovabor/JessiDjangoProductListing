import django_filters
from .models import Listing

class ListingFilter(django_filters.FilterSet):
    class Meta:
        model = Listing
        fields = {'brands':{'exact'}, 'transmission':{'exact'}, 'fuel_type':{'exact'}, 'body_type':{'exact'}, 'mileage':{'lt'},'model':{'icontains'},}