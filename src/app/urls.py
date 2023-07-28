#defining the app urls
from django.urls import path
from app.views import main_view ,home_view , list_view,listing_view

urlpatterns = [
    
    path('',main_view,name='app'),
    path('home/',home_view,name='home'),
    path('list/', list_view ,name='list'),
    path('listing/<str:id>', listing_view ,name='listing')
    
]