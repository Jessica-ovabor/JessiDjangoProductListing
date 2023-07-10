#defining the app urls
from django.urls import path
from app.views import main_view ,home_view

urlpatterns = [
    
    path('',main_view,name='app'),
    path('home/',home_view,name='home'),
    
]